from pathlib import Path

from src.generate.template.render import read_template, replace_attribute_tag, replace_text_tag
from src.generate.tracks.models.track_info import TrackInfo
from .body import render_track_body


def render_html(*, track: "TrackInfo", repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / track.metadata.url / "index.html"

    body_html = render_track_body(track=track, repo_root=repo_root)

    layout_html = read_template(template_path=layout_path)

    track_html = replace_text_tag(
        template_html=layout_html, tag="body", value=body_html, escape=False
    )

    track_html = replace_attribute_tag(
        template_html=track_html, tag="path_prefix", value="../", escape=True
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(track_html, encoding="utf-8")
