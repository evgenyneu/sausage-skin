from pathlib import Path

from src.generate.process.cover.main import process_cover


def test_process_cover_calls_implementation(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    process_cover(track_dir=track_dir, repo_root=repo_root, url=url)

    cover_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover.jpg"
    thumb_dest = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"

    assert cover_dest.exists()
    assert thumb_dest.exists()
