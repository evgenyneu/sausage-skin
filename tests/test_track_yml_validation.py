from pathlib import Path

import pytest

from src.generate.yaml.main import read_track_yml


def test_validate_track_yml_missing_title(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """url: "test"
description: Some description
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_missing_description(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
url: "test"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'description'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_empty_title(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: ""
description: Some description
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_empty_description(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
url: "test"
description: ""
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'description'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_whitespace_title(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "   "
url: "test"
description: "test description"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_whitespace_description(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
url: "test"
description: "   "
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'description'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_missing_url(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
description: "test description"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'url'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_empty_url(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
url: ""
description: "test description"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'url'"):
        read_track_yml(track_yml_path=track_yml_path)


def test_validate_track_yml_whitespace_url(tmp_path: Path) -> None:
    track_yml_path = tmp_path / "track.yml"
    track_yml_path.write_text(
        """title: "test"
url: "   "
description: "test description"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required field 'url'"):
        read_track_yml(track_yml_path=track_yml_path)
