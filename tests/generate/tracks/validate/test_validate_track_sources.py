from pathlib import Path

import pytest

from src.generate.tracks.errors import TrackValidationError
from src.generate.tracks.validate import validate_track_sources


def test_validate_track_sources_ok(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song_mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "song_cover.jpg").write_text("data", encoding="utf-8")

    validate_track_sources(track_dir=track_dir)


def test_validate_track_sources_uses_correct_patterns(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "mix.wav").write_text("data", encoding="utf-8")
    (track_dir / "cover.jpg").write_text("data", encoding="utf-8")

    with pytest.raises(TrackValidationError, match=r"Missing mix wav file"):
        validate_track_sources(track_dir=track_dir)
