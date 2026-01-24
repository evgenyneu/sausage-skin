from pathlib import Path
from subprocess import run

from src.generate.process.thumb import THUMBNAIL_WIDTH, generate_thumbnail_for_track


def test_generate_thumbnail_for_track_creates_thumbnail_with_width_600(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[4]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    thumbnail = generate_thumbnail_for_track(track_dir=track_dir, url=url, repo_root=repo_root)

    assert thumbnail.exists()
    assert thumbnail == repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"

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

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    existing_thumb = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"
    existing_thumb.parent.mkdir(parents=True, exist_ok=True)
    existing_thumb.write_bytes(b"thumb")

    thumbnail = generate_thumbnail_for_track(track_dir=track_dir, url=url, repo_root=repo_root)

    assert thumbnail == existing_thumb

    content = existing_thumb.read_bytes()

    assert content == b"thumb"
