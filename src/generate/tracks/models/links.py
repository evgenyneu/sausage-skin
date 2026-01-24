from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Links:
    youtube: str | None = None
    soundcloud: str | None = None
    bandcamp: str | None = None
