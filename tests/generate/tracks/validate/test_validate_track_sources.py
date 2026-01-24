from pathlib import Path

import pytest

from src.generate.tracks.validate import validate_track_sources


def test_validate_track_sources_ok(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song_mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "song_cover.jpg").write_text("data", encoding="utf-8")

    validate_track_sources(track_dir=track_dir)


def test_validate_track_sources_missing_mix(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song_cover.jpg").write_text("data", encoding="utf-8")

    with pytest.raises(ValueError, match="Missing mix wav file"):
        validate_track_sources(track_dir=track_dir)


def test_validate_track_sources_missing_cover(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song_mix.wav").write_text("data", encoding="utf-8")

    with pytest.raises(ValueError, match="Missing cover image"):
        validate_track_sources(track_dir=track_dir)


def test_validate_track_sources_multiple_mix(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "a_mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "b_mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "song_cover.jpg").write_text("data", encoding="utf-8")

    with pytest.raises(ValueError, match="multiple mix wav file"):
        validate_track_sources(track_dir=track_dir)


def test_validate_track_sources_multiple_cover(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song_mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "a_cover.jpg").write_text("data", encoding="utf-8")
    (track_dir / "b_cover.jpg").write_text("data", encoding="utf-8")

    with pytest.raises(ValueError, match="multiple cover image"):
        validate_track_sources(track_dir=track_dir)
