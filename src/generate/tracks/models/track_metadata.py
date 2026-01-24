from __future__ import annotations

from dataclasses import dataclass

from .album import Album
from .links import Links


@dataclass
class TrackMetadata:
    title: str
    url: str
    album: Album | None = None
    links: Links | None = None
    description: str | None = None
    isrc: str | None = None
