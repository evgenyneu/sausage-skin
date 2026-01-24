from datetime import date as date_type
from pathlib import Path

from src.generate.process.single import process_single_track
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.yaml.main import TrackMetadata


def test_process_single_track_no_error(tmp_path: Path) -> None:
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

    process_single_track(track=track, repo_root=repo_root)

    thumbnail = repo_root / "src" / "web" / "tracks" / url / "images" / "cover_600.jpg"

    assert thumbnail.exists()
