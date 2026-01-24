from pathlib import Path
from subprocess import CalledProcessError, run

from src.generate.errors import ProgramError

THUMBNAIL_SIZES = {
    "small": 600,
    "medium": 1200,
}

THUMBNAIL_WIDTH = 600
JPEG_QUALITY = 3


def build_thumbnail_command(
    *, cover: Path, thumbnail: Path, width: int = THUMBNAIL_WIDTH, quality: int = JPEG_QUALITY
) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-i",
        str(cover),
        "-vf",
        f"scale={width}:-1",
        "-q:v",
        str(quality),
        str(thumbnail),
    ]


def generate_thumbnail(
    *, cover: Path, thumbnail: Path, width: int = THUMBNAIL_WIDTH, quality: int = JPEG_QUALITY
) -> None:
    command = build_thumbnail_command(
        cover=cover, thumbnail=thumbnail, width=width, quality=quality
    )

    try:
        run(command, check=True, capture_output=True)
    except CalledProcessError as error:
        stderr = error.stderr.decode(errors="ignore") if error.stderr else ""
        message = f"Failed to generate thumbnail for {cover}: {stderr.strip()}"

        raise ProgramError(message) from error


def generate_all_thumbs(*, cover: Path, images_dir: Path) -> None:
    for thumb_name, width in THUMBNAIL_SIZES.items():
        thumb_path = images_dir / f"cover_{width}.jpg"

        if not thumb_path.exists():
            generate_thumbnail(cover=cover, thumbnail=thumb_path, width=width)
