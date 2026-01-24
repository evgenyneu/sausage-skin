from __future__ import annotations

from pathlib import Path

from yaml import safe_load

from .validate import validate_track_yml
from src.generate.tracks.models.album import Album
from src.generate.tracks.models.links import Links
from src.generate.tracks.models.track_metadata import TrackMetadata


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
        url=data.get("url", ""),
        album=album,
        links=links,
        description=data.get("description"),
        isrc=data.get("isrc"),
    )
