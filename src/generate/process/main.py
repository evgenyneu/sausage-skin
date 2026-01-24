from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
from os import cpu_count

from src.generate.tracks.tracks import TrackInfo


def process_single_track(*, track: TrackInfo) -> None:
    print(f"Processing track {track.track_dir}")


def process_tracks(*, tracks: list[TrackInfo]) -> None:
    max_workers = min(4, cpu_count() or 1)

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_track, track=track): track for track in tracks}

        for future in as_completed(futures):
            track = futures[future]

            try:
                future.result()
            except Exception as e:
                raise RuntimeError(f"Failed to process track {track.track_dir}: {e}") from e
