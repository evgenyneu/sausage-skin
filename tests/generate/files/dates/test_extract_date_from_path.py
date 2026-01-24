from datetime import date as date_type
from pathlib import Path

from src.generate.tracks.dates import extract_date_from_path


def test_extract_date_from_path() -> None:
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a11_nov" / "a05_cloven_hoofed"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 11, 5)


def test_extract_date_from_path_single_digit_month() -> None:
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a06_jun" / "a20_deadlift"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 6, 20)


def test_extract_date_from_path_single_digit_day() -> None:
    music_root = Path("/music")
    track_dir = music_root / "a2024" / "a07_jul" / "a05_overhead_press"

    result_date = extract_date_from_path(track_dir, music_root)

    assert result_date == date_type(2024, 7, 5)
