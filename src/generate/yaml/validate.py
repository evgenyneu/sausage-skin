from __future__ import annotations

from pathlib import Path


def require_non_blank(*, data: dict, key: str, track_yml_path: Path) -> None:
    value = data.get(key)

    if not value or not str(value).strip():
        raise ValueError(f"Missing required field '{key}' in {track_yml_path}")


def validate_track_yml(*, data: dict, track_yml_path: Path) -> None:
    require_non_blank(data=data, key="title", track_yml_path=track_yml_path)
    require_non_blank(data=data, key="description", track_yml_path=track_yml_path)
    require_non_blank(data=data, key="url", track_yml_path=track_yml_path)
