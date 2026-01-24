from pathlib import Path

from src.generate.tracks.models.track_info import TrackInfo
from .copy import copy_tracks_cache
from .process import process_tracks as process_tracks_impl


def process_tracks(*, tracks: list[TrackInfo], repo_root: Path) -> None:
    process_tracks_impl(tracks=tracks, repo_root=repo_root)
    copy_tracks_cache(repo_root=repo_root)
