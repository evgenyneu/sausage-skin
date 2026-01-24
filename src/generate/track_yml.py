from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from yaml import safe_load


@dataclass
class Album:
    track_number: int | None = None
    name: str | None = None


@dataclass
class Links:
    youtube: str | None = None
    soundcloud: str | None = None
    bandcamp: str | None = None


@dataclass
class TrackMetadata:
    title: str
    album: Album | None = None
    links: Links | None = None
    description: str | None = None
    isrc: str | None = None
    url: str | None = None


def validate_track_yml(*, data: dict, track_yml_path: Path) -> None:
    title = data.get("title")
    if not title or not str(title).strip():
        raise ValueError(f"Missing required field 'title' in {track_yml_path}")

    description = data.get("description")
    if not description or not str(description).strip():
        raise ValueError(f"Missing required field 'description' in {track_yml_path}")


def read_track_yml(*, track_yml_path: Path) -> TrackMetadata:
    content = track_yml_path.read_text(encoding="utf-8")
    data = safe_load(content) or {}

    validate_track_yml(data=data, track_yml_path=track_yml_path)

    album_data = data.get("album", {})

    album = (
        Album(
            track_number=album_data.get("track_number"),
            name=album_data.get("name"),
        )
        if album_data
        else None
    )

    links_data = data.get("links", {})

    links = (
        Links(
            youtube=links_data.get("youtube"),
            soundcloud=links_data.get("soundcloud"),
            bandcamp=links_data.get("bandcamp"),
        )
        if links_data
        else None
    )

    return TrackMetadata(
        title=data.get("title", ""),
        album=album,
        links=links,
        description=data.get("description"),
        isrc=data.get("isrc"),
        url=data.get("url"),
    )
