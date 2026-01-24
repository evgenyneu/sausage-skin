from __future__ import annotations

from pathlib import Path

from src.generate.tracks.models.track_info import TrackInfo

from .tracks import discover_tracks as discover_tracks_impl
from .urls import ensure_unique_urls


def discover_tracks(*, music_root: Path) -> list[TrackInfo]:
    tracks = discover_tracks_impl(music_root=music_root)

    ensure_unique_urls(tracks=tracks)

    return tracks
