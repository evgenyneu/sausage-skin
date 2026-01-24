from pathlib import Path

from .body import render_track_body
from src.generate.tracks.models.track_info import TrackInfo


def render_html(*, track: "TrackInfo", repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / track.metadata.url / "index.html"

    layout_html = layout_path.read_text(encoding="utf-8")

    body_html = render_track_body(track=track, repo_root=repo_root)

    track_html = layout_html.replace("{{ body }}", body_html)
    track_html = track_html.replace("{{ path_prefix }}", "../")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(track_html, encoding="utf-8")
