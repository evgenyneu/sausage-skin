from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .track_metadata import TrackMetadata


@dataclass
class TrackInfo:
    track_dir: Path
    track_yml_path: Path
    date: date
    metadata: TrackMetadata
