from pathlib import Path
from subprocess import run

from src.generate.process.cover.cover import process_cover as process_cover_impl


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
    thumb_600_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"
    thumb_1200_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_1200.jpg"

    assert cover_dest.exists()
    assert thumb_600_dest.exists()
    assert thumb_1200_dest.exists()

    result_600 = run(
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
            str(thumb_600_dest),
        ],
        check=True,
        capture_output=True,
    )

    width_600_str = result_600.stdout.decode().strip()

    assert width_600_str == "600"

    result_1200 = run(
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
            str(thumb_1200_dest),
        ],
        check=True,
        capture_output=True,
    )

    width_1200_str = result_1200.stdout.decode().strip()

    assert width_1200_str == "1200"


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
    thumb_600_dest = images_dir / "cover_600.jpg"
    thumb_1200_dest = images_dir / "cover_1200.jpg"

    cover_dest.write_bytes(cover_source.read_bytes())
    thumb_600_dest.write_bytes(b"thumb-600-bytes")
    thumb_1200_dest.write_bytes(b"thumb-1200-bytes")

    process_cover_impl(track_dir=track_dir, repo_root=repo_root, url=url)

    assert cover_dest.read_bytes() == cover_source.read_bytes()
    assert thumb_600_dest.read_bytes() == b"thumb-600-bytes"
    assert thumb_1200_dest.read_bytes() == b"thumb-1200-bytes"
