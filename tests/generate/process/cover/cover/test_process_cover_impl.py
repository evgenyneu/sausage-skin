from pathlib import Path
from subprocess import run

from src.generate.process.cover.cover import process_cover as process_cover_impl
from src.generate.process.cover.thumb import THUMBNAIL_WIDTH


def test_process_cover_creates_cover_and_thumbnail_with_width_600(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    process_cover_impl(track_dir=track_dir, repo_root=repo_root, url=url)

    cover_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover.jpg"
    thumb_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"

    assert cover_dest.exists()
    assert thumb_dest.exists()

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
            str(thumb_dest),
        ],
        check=True,
        capture_output=True,
    )

    width_str = result.stdout.decode().strip()

    assert width_str == str(THUMBNAIL_WIDTH)


def test_process_cover_skips_when_assets_exist(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    images_dir = repo_root / "src" / "web" / "tracks" / url / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    cover_dest = images_dir / "cover.jpg"
    thumb_dest = images_dir / "cover_600.jpg"

    cover_dest.write_bytes(b"cover-bytes")
    thumb_dest.write_bytes(b"thumb-bytes")

    process_cover_impl(track_dir=track_dir, repo_root=repo_root, url=url)

    assert cover_dest.read_bytes() == b"cover-bytes"
    assert thumb_dest.read_bytes() == b"thumb-bytes"
