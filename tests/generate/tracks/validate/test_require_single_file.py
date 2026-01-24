from pathlib import Path

import pytest

from src.generate.tracks.errors import TrackValidationError
from src.generate.tracks.validate import require_single_file


def test_require_single_file_ok(tmp_path: Path) -> None:
    directory = tmp_path / "dir"
    directory.mkdir()

    target = directory / "foo_mix.wav"
    target.write_text("data", encoding="utf-8")

    result = require_single_file(
        directory=directory,
        pattern="*_mix.wav",
        description="mix wav file",
    )

    assert result == target


def test_require_single_file_missing(tmp_path: Path) -> None:
    directory = tmp_path / "dir"
    directory.mkdir()

    with pytest.raises(TrackValidationError, match="Missing mix wav file"):
        require_single_file(
            directory=directory,
            pattern="*_mix.wav",
            description="mix wav file",
        )


def test_require_single_file_multiple(tmp_path: Path) -> None:
    directory = tmp_path / "dir"
    directory.mkdir()

    (directory / "a_mix.wav").write_text("data", encoding="utf-8")
    (directory / "b_mix.wav").write_text("data", encoding="utf-8")

    with pytest.raises(TrackValidationError, match="multiple mix wav file"):
        require_single_file(
            directory=directory,
            pattern="*_mix.wav",
            description="mix wav file",
        )
