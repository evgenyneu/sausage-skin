from datetime import date as date_type
from pathlib import Path

from src.generate.process.main import process_tracks
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.yaml.main import TrackMetadata


def test_process_tracks_empty_list(tmp_path: Path) -> None:
    repo_root = tmp_path

    src_tracks = repo_root / "src" / "web" / "tracks"
    src_tracks.mkdir(parents=True, exist_ok=True)

    process_tracks(tracks=[], repo_root=repo_root)

    web_tracks = repo_root / "web" / "tracks"

    assert web_tracks.exists()


def test_process_tracks_single_track(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[4]
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    music_root = repo_root / "music"
    track_dir = music_root / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)
    track_yml_path = track_dir / "track.yml"

    cover = track_dir / "song_cover.jpg"
    cover.write_bytes(cover_source.read_bytes())

    url = "test-track"

    track = TrackInfo(
        track_dir=track_dir,
        track_yml_path=track_yml_path,
        date=date_type(2024, 1, 1),
        metadata=TrackMetadata(
            title="test",
            url=url,
            description="test description",
        ),
    )

    web_dir = repo_root / "web"
    old_file = web_dir / "old-file.txt"
    old_subdir = web_dir / "old-dir"
    old_subfile = old_subdir / "old-sub.txt"

    old_subdir.mkdir(parents=True, exist_ok=True)
    old_file.write_text("old-content", encoding="utf-8")
    old_subfile.write_text("old-sub-content", encoding="utf-8")

    assert old_file.exists()
    assert old_subfile.exists()

    process_tracks(tracks=[track], repo_root=repo_root)

    assert not old_file.exists()
    assert not old_subdir.exists()

    thumbnail = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"

    assert thumbnail.exists()

    web_thumbnail = repo_root / "web" / "tracks" / url / "images" / "cover_600.jpg"
    web_cover = repo_root / "web" / "tracks" / url / "images" / "cover.jpg"

    assert web_thumbnail.exists()
    assert web_cover.exists()

    assert web_thumbnail.read_bytes() == thumbnail.read_bytes()

    assert (
        web_cover.read_bytes()
        == (repo_root / "src" / "web" / "tracks" / url / "images" / "cover.jpg").read_bytes()
    )
