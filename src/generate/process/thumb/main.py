from pathlib import Path
from subprocess import CalledProcessError, run

from src.generate.errors import ProgramError
from src.generate.tracks.validate import require_single_file


THUMBNAIL_WIDTH = 400


def build_thumbnail_command(
    *, cover: Path, thumbnail: Path, width: int = THUMBNAIL_WIDTH
) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-i",
        str(cover),
        "-vf",
        f"scale={width}:-1",
        str(thumbnail),
    ]


def find_cover_image(*, track_dir: Path) -> Path:
    return require_single_file(
        directory=track_dir,
        pattern="*_cover.jpg",
        description="cover image",
    )


def generate_thumbnail(*, cover: Path, thumbnail: Path, width: int = THUMBNAIL_WIDTH) -> None:
    command = build_thumbnail_command(cover=cover, thumbnail=thumbnail, width=width)

    try:
        run(command, check=True, capture_output=True)
    except CalledProcessError as error:
        stderr = error.stderr.decode(errors="ignore") if error.stderr else ""
        message = f"Failed to generate thumbnail for {cover}: {stderr.strip()}"

        raise ProgramError(message) from error


def generate_thumbnail_for_track(*, track_dir: Path, width: int = THUMBNAIL_WIDTH) -> Path:
    cover = find_cover_image(track_dir=track_dir)
    thumbnail = cover.with_name(f"{cover.stem}_{width}{cover.suffix}")

    if not thumbnail.exists():
        generate_thumbnail(cover=cover, thumbnail=thumbnail, width=width)

    return thumbnail
