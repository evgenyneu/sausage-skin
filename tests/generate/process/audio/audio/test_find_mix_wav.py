from pathlib import Path

import pytest

from src.generate.process.audio.audio import find_mix_wav
from src.generate.tracks.errors import TrackValidationError


def test_find_mix_wav_ok(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    wav_file = track_dir / "song_mix.wav"
    wav_file.write_text("data", encoding="utf-8")

    result = find_mix_wav(track_dir=track_dir)

    assert result == wav_file


def test_find_mix_wav_missing(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    with pytest.raises(TrackValidationError, match=r"Missing mix wav file"):
        find_mix_wav(track_dir=track_dir)


def test_find_mix_wav_multiple(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    (track_dir / "song1_mix.wav").write_text("data1", encoding="utf-8")
    (track_dir / "song2_mix.wav").write_text("data2", encoding="utf-8")

    with pytest.raises(TrackValidationError, match=r"Found multiple mix wav file"):
        find_mix_wav(track_dir=track_dir)
