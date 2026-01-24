from datetime import date as date_type
from pathlib import Path

import pytest

from src.generate.tracks.tracks import TrackInfo
from src.generate.tracks.urls import ensure_unique_urls
from src.generate.yaml.main import TrackMetadata


def build_track(path: str, url: str, title: str = "title") -> TrackInfo:
    return TrackInfo(
        track_dir=Path(path),
        track_yml_path=Path(path) / "track.yml",
        date=date_type(2024, 6, 20),
        metadata=TrackMetadata(
            title=title,
            url=url,
            description="test",
        ),
    )


def test_ensure_unique_urls_ok() -> None:
    track1 = build_track("/music/a2024/a06_jun/a20_deadlift", "deadlift")
    track2 = build_track("/music/a2024/a06_jun/a21_squats", "squats")

    ensure_unique_urls(tracks=[track1, track2])


def test_ensure_unique_urls_duplicate() -> None:
    track1 = build_track("/music/a2024/a06_jun/a20_deadlift", "deadlift", title="deadlift")
    track2 = build_track(
        "/music/a2024/a06_jun/a21_squats",
        "deadlift",
        title="deadlift again",
    )

    with pytest.raises(ValueError, match="Duplicate url 'deadlift'"):
        ensure_unique_urls(tracks=[track1, track2])
