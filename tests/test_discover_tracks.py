from datetime import date as date_type
from pathlib import Path

import pytest

from src.generate.discover_tracks import (
    TrackInfo,
    discover_tracks,
    ensure_unique_urls,
    extract_date_from_path,
)
from src.generate.yaml.main import TrackMetadata


def test_extract_date_from_path():
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a11_nov" / "a05_cloven_hoofed"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 11, 5)


def test_extract_date_from_path_single_digit_month():
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a06_jun" / "a20_deadlift"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 6, 20)


def test_extract_date_from_path_single_digit_day():
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a07_jul" / "a05_overhead_press"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 7, 5)


def test_discover_tracks(tmp_path):
    music_root = tmp_path / "music"
    music_root.mkdir()

    track_dir = music_root / "a2024" / "a11_nov" / "a05_cloven_hoofed"
    track_dir.mkdir(parents=True)
    (track_dir / "track.yml").write_text(
        'title: "test"\nurl: "test"\ndescription: "test description"'
    )

    no_track_dir = music_root / "a2024" / "a11_nov" / "a06_no_track"
    no_track_dir.mkdir(parents=True)

    tracks = discover_tracks(music_root=music_root)

    assert len(tracks) == 1
    assert tracks[0].track_dir == track_dir
    assert tracks[0].track_yml_path == track_dir / "track.yml"
    assert tracks[0].date == date_type(2024, 11, 5)
    assert tracks[0].metadata.title == "test"


def test_ensure_unique_urls_ok() -> None:
    track1 = TrackInfo(
        track_dir=Path("/music/a2024/a06_jun/a20_deadlift"),
        track_yml_path=Path("/music/a2024/a06_jun/a20_deadlift/track.yml"),
        date=date_type(2024, 6, 20),
        metadata=TrackMetadata(
            title="deadlift",
            url="deadlift",
            description="test",
        ),
    )

    track2 = TrackInfo(
        track_dir=Path("/music/a2024/a06_jun/a21_squats"),
        track_yml_path=Path("/music/a2024/a06_jun/a21_squats/track.yml"),
        date=date_type(2024, 6, 21),
        metadata=TrackMetadata(
            title="squats",
            url="squats",
            description="test",
        ),
    )

    ensure_unique_urls(tracks=[track1, track2])


def test_ensure_unique_urls_duplicate() -> None:
    track1 = TrackInfo(
        track_dir=Path("/music/a2024/a06_jun/a20_deadlift"),
        track_yml_path=Path("/music/a2024/a06_jun/a20_deadlift/track.yml"),
        date=date_type(2024, 6, 20),
        metadata=TrackMetadata(
            title="deadlift",
            url="deadlift",
            description="test",
        ),
    )

    track2 = TrackInfo(
        track_dir=Path("/music/a2024/a06_jun/a21_squats"),
        track_yml_path=Path("/music/a2024/a06_jun/a21_squats/track.yml"),
        date=date_type(2024, 6, 21),
        metadata=TrackMetadata(
            title="deadlift again",
            url="deadlift",
            description="test",
        ),
    )

    with pytest.raises(ValueError, match="Duplicate url 'deadlift'"):
        ensure_unique_urls(tracks=[track1, track2])
