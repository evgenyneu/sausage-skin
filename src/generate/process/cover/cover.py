from pathlib import Path
from shutil import copy2

from src.generate.tracks.validate import require_single_file
from .thumb import generate_all_thumbs


def find_cover_image(*, track_dir: Path) -> Path:
    return require_single_file(
        directory=track_dir,
        pattern="*_cover.jpg",
        description="cover image",
    )


def build_cover_output_path(*, repo_root: Path, url: str) -> Path:
    images_dir = repo_root / "src" / "web" / "tracks" / url / "images"
    return images_dir / "cover.jpg"


def process_cover(*, track_dir: Path, repo_root: Path, url: str) -> None:
    source_cover = find_cover_image(track_dir=track_dir)

    cover_path = build_cover_output_path(repo_root=repo_root, url=url)
    images_dir = cover_path.parent
    images_dir.mkdir(parents=True, exist_ok=True)

    if not cover_path.exists():
        copy2(source_cover, cover_path)

    generate_all_thumbs(cover=cover_path, images_dir=images_dir)
