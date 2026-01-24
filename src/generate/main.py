from pathlib import Path

from .index_html import generate_index_html
from .process.main import process_tracks
from .tracks.main import discover_tracks


def main(
    repo_root: Path | None = None,
    music_root: Path | None = None,
) -> None:
    if repo_root is None:
        repo_root = Path.cwd()

    if music_root is None:
        music_root = repo_root / "music"

    tracks = discover_tracks(music_root=music_root)

    print(f"Discovered {len(tracks)} tracks")

    process_tracks(tracks=tracks)

    generate_index_html(repo_root=repo_root)


if __name__ == "__main__":
    main()
