from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from re import match

from .yaml.main import TrackMetadata, read_track_yml


@dataclass
class TrackInfo:
    track_dir: Path
    track_yml_path: Path
    date: date
    metadata: TrackMetadata


def extract_date_from_path(track_dir: Path, music_root: Path) -> date:
    relative = track_dir.relative_to(music_root)
    parts = relative.parts

    if len(parts) < 3:
        raise ValueError(f"Invalid track path structure: {relative}")

    year_part = parts[0]
    month_part = parts[1]
    day_part = parts[2]

    year_match = match(r"^a(\d{4})$", year_part)
    month_match = match(r"^a(\d{1,2})_", month_part)
    day_match = match(r"^a(\d{1,2})_", day_part)

    if not year_match or not month_match or not day_match:
        raise ValueError(f"Invalid date format in path: {relative}")

    year = int(year_match.group(1))
    month = int(month_match.group(1))
    day = int(day_match.group(1))

    return date(year, month, day)


def discover_tracks(*, music_root: Path) -> list[TrackInfo]:
    tracks = []

    for track_dir in music_root.rglob("*"):
        if not track_dir.is_dir():
            continue

        track_yml_path = track_dir / "track.yml"

        if not track_yml_path.exists():
            continue

        date = extract_date_from_path(track_dir, music_root)
        metadata = read_track_yml(track_yml_path=track_yml_path)

        tracks.append(
            TrackInfo(
                track_dir=track_dir,
                track_yml_path=track_yml_path,
                date=date,
                metadata=metadata,
            )
        )

    return tracks


def ensure_unique_urls(*, tracks: list[TrackInfo]) -> None:
    seen: dict[str, TrackInfo] = {}

    for track in tracks:
        url = track.metadata.url

        if url in seen:
            other = seen[url]

            raise ValueError(
                f"Duplicate url '{url}' for tracks {other.track_dir} and {track.track_dir}"
            )

        seen[url] = track
