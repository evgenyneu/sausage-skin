from pathlib import Path
from shutil import copytree

from src.generate.errors import ProgramError


def copy_tracks_cache(*, repo_root: Path) -> None:
    src_tracks = repo_root / "src" / "web" / "tracks"
    web_dir = repo_root / "web"

    if not src_tracks.exists():
        raise ProgramError(f"Source tracks directory does not exist: {src_tracks}")

    for track_dir in src_tracks.iterdir():
        if track_dir.is_dir():
            dest_dir = web_dir / track_dir.name
            copytree(track_dir, dest_dir)
