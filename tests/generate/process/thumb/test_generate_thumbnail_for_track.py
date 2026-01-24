from pathlib import Path
from subprocess import run

from src.generate.process.thumb.main import THUMBNAIL_WIDTH, generate_thumbnail_for_track


def test_generate_thumbnail_for_track_creates_thumbnail_with_width_600(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[4]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    track_dir = tmp_path / "track"
    track_dir.mkdir()

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    thumbnail = generate_thumbnail_for_track(track_dir=track_dir)

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


def test_generate_thumbnail_for_track_skips_when_exists(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[4]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    track_dir = tmp_path / "track"
    track_dir.mkdir()

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    existing_thumb = track_dir / "song_cover_600.jpg"
    existing_thumb.write_bytes(b"thumb")

    thumbnail = generate_thumbnail_for_track(track_dir=track_dir)

    assert thumbnail == existing_thumb

    content = existing_thumb.read_bytes()

    assert content == b"thumb"
