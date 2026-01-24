from pathlib import Path
from .discover_tracks import discover_tracks
from .index_html import generate_index_html


def main() -> None:
    repo_root = Path.cwd()

    music_root = repo_root / "music"
    tracks = discover_tracks(music_root=music_root)

    print(f"Discovered {len(tracks)} tracks")

    generate_index_html(repo_root=repo_root)


if __name__ == "__main__":
    main()
