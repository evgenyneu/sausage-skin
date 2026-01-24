from pathlib import Path

from .index_html import generate_index_html
from .process.main import process_tracks
from .tracks.errors import TrackValidationError
from .tracks.main import discover_tracks
from .yaml.errors import YamlValidationError


def main(
    repo_root: Path | None = None,
    music_root: Path | None = None,
) -> None:
    if repo_root is None:
        repo_root = Path.cwd()

    if music_root is None:
        music_root = repo_root / "music"

    try:
        tracks = discover_tracks(music_root=music_root)
        print(f"Discovered {len(tracks)} tracks")
        process_tracks(tracks=tracks)
        generate_index_html(repo_root=repo_root)
    except (TrackValidationError, YamlValidationError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
