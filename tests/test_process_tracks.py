from datetime import date as date_type
from pathlib import Path

from src.generate.discover_tracks import TrackInfo
from src.generate.process.main import process_tracks
from src.generate.track_yml import TrackMetadata


def test_process_tracks_empty_list() -> None:
    process_tracks(tracks=[])


def test_process_tracks_single_track(tmp_path: Path) -> None:
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

    process_tracks(tracks=[track])
