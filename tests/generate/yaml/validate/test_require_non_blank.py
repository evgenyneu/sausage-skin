from pathlib import Path

import pytest

from src.generate.yaml.validate import require_non_blank


def test_require_non_blank_ok() -> None:
    data = {"title": "test"}

    require_non_blank(data=data, key="title", track_yml_path=Path("track.yml"))


def test_require_non_blank_missing_key() -> None:
    data = {}

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        require_non_blank(data=data, key="title", track_yml_path=Path("track.yml"))


def test_require_non_blank_empty_string() -> None:
    data = {"title": ""}

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        require_non_blank(data=data, key="title", track_yml_path=Path("track.yml"))


def test_require_non_blank_whitespace() -> None:
    data = {"title": "   "}

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        require_non_blank(data=data, key="title", track_yml_path=Path("track.yml"))
