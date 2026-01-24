from __future__ import annotations

from pathlib import Path

from .tracks import TrackInfo, discover_tracks as discover_tracks_impl
from .urls import ensure_unique_urls


def discover_tracks(*, music_root: Path) -> list[TrackInfo]:
    tracks = discover_tracks_impl(music_root=music_root)

    ensure_unique_urls(tracks=tracks)

    return tracks
