from pathlib import Path

from src.generate.process.cover.main import process_cover
from src.generate.tracks.models.track_info import TrackInfo


def process_single_track(*, track: TrackInfo, repo_root: Path) -> None:
    print(f"Processing track {track.track_dir}")

    process_cover(
        track_dir=track.track_dir,
        repo_root=repo_root,
        url=track.metadata.url,
    )
