from pathlib import Path

from src.generate.template.render import read_template, replace_attribute_tag, replace_text_tag
from src.generate.tracks.models.track_info import TrackInfo
from .assets import copy_web_assets
from .grid import render_track_grid


def render_html(*, tracks: list[TrackInfo], repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / "index.html"

    body_html = render_track_grid(tracks=tracks, repo_root=repo_root)

    layout_html = read_template(template_path=layout_path)

    index_html = replace_text_tag(
        template_html=layout_html, tag="body", value=body_html, escape=False
    )

    index_html = replace_attribute_tag(
        template_html=index_html, tag="path_prefix", value="", escape=True
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(index_html, encoding="utf-8")

    copy_web_assets(repo_root=repo_root)
