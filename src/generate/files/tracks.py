from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from src.generate.yaml.main import TrackMetadata, read_track_yml

from .dates import extract_date_from_path


@dataclass
class TrackInfo:
    track_dir: Path
    track_yml_path: Path
    date: date
    metadata: TrackMetadata


def discover_tracks(*, music_root: Path) -> list[TrackInfo]:
    tracks: list[TrackInfo] = []

    for track_dir in music_root.rglob("*"):
        if not track_dir.is_dir():
            continue

        track_yml_path = track_dir / "track.yml"

        if not track_yml_path.exists():
            continue

        track_date = extract_date_from_path(track_dir, music_root)
        metadata = read_track_yml(track_yml_path=track_yml_path)

        tracks.append(
            TrackInfo(
                track_dir=track_dir,
                track_yml_path=track_yml_path,
                date=track_date,
                metadata=metadata,
            )
        )

    return tracks
