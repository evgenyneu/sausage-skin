from pathlib import Path
from subprocess import run

from src.generate.process.cover.thumb import THUMBNAIL_WIDTH, generate_thumbnail


def test_generate_thumbnail_creates_image_with_width_600(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    cover = tmp_path / "cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    thumbnail = tmp_path / "thumb.jpg"

    generate_thumbnail(cover=cover, thumbnail=thumbnail)

    assert thumbnail.exists()

    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width",
            "-of",
            "csv=p=0",
            str(thumbnail),
        ],
        check=True,
        capture_output=True,
    )

    width_str = result.stdout.decode().strip()

    assert width_str == str(THUMBNAIL_WIDTH)
