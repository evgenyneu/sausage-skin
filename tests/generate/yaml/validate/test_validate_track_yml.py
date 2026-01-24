from pathlib import Path

import pytest

from src.generate.yaml.validate import validate_track_yml


def test_validate_track_yml_missing_title() -> None:
    data = {
        "url": "test",
        "description": "Some description",
    }

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        validate_track_yml(data=data, track_yml_path=Path("track.yml"))


def test_validate_track_yml_missing_description() -> None:
    data = {
        "title": "test",
        "url": "test",
    }

    with pytest.raises(ValueError, match="Missing required field 'description'"):
        validate_track_yml(data=data, track_yml_path=Path("track.yml"))


def test_validate_track_yml_missing_url() -> None:
    data = {
        "title": "test",
        "description": "test description",
    }

    with pytest.raises(ValueError, match="Missing required field 'url'"):
        validate_track_yml(data=data, track_yml_path=Path("track.yml"))


def test_validate_track_yml_empty_fields() -> None:
    data = {"title": "", "url": "", "description": ""}

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        validate_track_yml(data=data, track_yml_path=Path("track.yml"))


def test_validate_track_yml_whitespace_fields() -> None:
    data = {"title": "   ", "url": "   ", "description": "   "}

    with pytest.raises(ValueError, match="Missing required field 'title'"):
        validate_track_yml(data=data, track_yml_path=Path("track.yml"))
