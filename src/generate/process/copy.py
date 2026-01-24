from pathlib import Path
from shutil import copytree

from src.generate.errors import ProgramError


def copy_tracks_cache(*, repo_root: Path) -> None:
    src_tracks = repo_root / "src" / "web" / "tracks"
    web_tracks = repo_root / "web" / "tracks"

    if not src_tracks.exists():
        raise ProgramError(f"Source tracks directory does not exist: {src_tracks}")

    copytree(src_tracks, web_tracks)
