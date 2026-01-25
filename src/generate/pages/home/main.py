from pathlib import Path
from typing import TYPE_CHECKING

from .html import render_html as render_html_impl

if TYPE_CHECKING:
    from src.generate.tracks.models.track_info import TrackInfo


def render_html(*, tracks: list["TrackInfo"], repo_root: Path) -> None:
    render_html_impl(tracks=tracks, repo_root=repo_root)
