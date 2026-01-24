from concurrent.futures import ProcessPoolExecutor, as_completed
from os import cpu_count
from pathlib import Path

from src.generate.tracks.models.track_info import TrackInfo

from .single import process_single_track


def process_tracks(*, tracks: list[TrackInfo], repo_root: Path) -> None:
    max_workers = min(8, cpu_count() or 1)

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_single_track, track=track, repo_root=repo_root): track
            for track in tracks
        }

        for future in as_completed(futures):
            track = futures[future]

            try:
                future.result()
            except Exception as e:
                raise RuntimeError(f"Failed to process track {track.track_dir}: {e}") from e
