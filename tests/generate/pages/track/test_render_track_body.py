from pathlib import Path
from datetime import date

from src.generate.pages.track.main import render_track_body
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_track_body() -> None:
    track = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a01_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a01_test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test Track",
            url="test-track",
            description="test description",
        ),
    )

    result = render_track_body(track=track)

    assert 'src="images/cover.jpg"' in result
    assert 'alt="Sausage Skin - Test Track"' in result
    assert "<img" in result
