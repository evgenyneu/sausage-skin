from pathlib import Path

from src.generate.tracks.models.track_info import TrackInfo
from .assets import copy_web_assets
from .grid import render_track_grid


def render_html(*, tracks: list[TrackInfo], repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / "index.html"

    layout_html = layout_path.read_text(encoding="utf-8")

    body_html = render_track_grid(tracks=tracks)

    index_html = layout_html.replace("{{ body }}", body_html)
    index_html = index_html.replace("{{ path_prefix }}", "")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(index_html, encoding="utf-8")

    copy_web_assets(repo_root=repo_root)
