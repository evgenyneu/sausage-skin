from pathlib import Path

from .cover import process_cover as process_cover_impl


def process_cover(*, track_dir: Path, repo_root: Path, url: str) -> None:
    process_cover_impl(track_dir=track_dir, repo_root=repo_root, url=url)
