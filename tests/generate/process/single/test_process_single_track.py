from datetime import date as date_type
from pathlib import Path

from src.generate.tracks.models.track_info import TrackInfo
from src.generate.process.single import process_single_track
from src.generate.yaml.main import TrackMetadata


def test_process_single_track_no_error(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()
    track_yml_path = track_dir / "track.yml"

    track = TrackInfo(
        track_dir=track_dir,
        track_yml_path=track_yml_path,
        date=date_type(2024, 1, 1),
        metadata=TrackMetadata(
            title="test",
            url="test",
            description="test description",
        ),
    )

    process_single_track(track=track)
