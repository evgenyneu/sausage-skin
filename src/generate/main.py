from pathlib import Path
from sys import exit as sys_exit

from .errors import ProgramError
from .pages.home import generate_index_html
from .process.main import process_tracks
from .tracks.main import discover_tracks


def main(
    repo_root: Path | None = None,
    music_root: Path | None = None,
) -> int:
    if repo_root is None:
        repo_root = Path.cwd()

    if music_root is None:
        music_root = repo_root / "music"

    try:
        tracks = discover_tracks(music_root=music_root)
        print(f"Discovered {len(tracks)} tracks")
        process_tracks(tracks=tracks, repo_root=repo_root)
        generate_index_html(repo_root=repo_root)
        return 0
    except ProgramError as error:
        print(f"Error: {error}")
        return 1


if __name__ == "__main__":
    sys_exit(main())
