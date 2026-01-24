from pathlib import Path
from typing import TYPE_CHECKING

from .html import render_html

if TYPE_CHECKING:
    from src.generate.tracks.models.track_info import TrackInfo


def render_html_for_tracks(*, tracks: list["TrackInfo"], repo_root: Path) -> None:
    for track in tracks:
        render_html(track=track, repo_root=repo_root)
