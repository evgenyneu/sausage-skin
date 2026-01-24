from pathlib import Path
from shutil import copy2

from src.generate.tracks.validate import require_single_file

from .thumb import THUMBNAIL_WIDTH, generate_thumbnail


def find_cover_image(*, track_dir: Path) -> Path:
    return require_single_file(
        directory=track_dir,
        pattern="*_cover.jpg",
        description="cover image",
    )


def build_cover_output_paths(*, repo_root: Path, url: str) -> tuple[Path, Path]:
    images_dir = repo_root / "src" / "web" / "tracks" / url / "images"

    cover_path = images_dir / "cover.jpg"
    thumb_path = images_dir / f"cover_{THUMBNAIL_WIDTH}.jpg"

    return cover_path, thumb_path


def process_cover(*, track_dir: Path, repo_root: Path, url: str) -> None:
    source_cover = find_cover_image(track_dir=track_dir)

    cover_path, thumb_path = build_cover_output_paths(repo_root=repo_root, url=url)
    cover_path.parent.mkdir(parents=True, exist_ok=True)

    if not cover_path.exists():
        copy2(source_cover, cover_path)

    if not thumb_path.exists():
        generate_thumbnail(cover=cover_path, thumbnail=thumb_path)
