from datetime import date as date_type
from pathlib import Path

from src.generate.discover_tracks import discover_tracks, extract_date_from_path


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
