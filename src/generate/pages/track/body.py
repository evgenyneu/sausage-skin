from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.tracks.models.track_info import TrackInfo


def render_track_body(*, track: "TrackInfo", repo_root: Path) -> str:
    template_path = repo_root / "src" / "generate" / "pages" / "track" / "templates" / "main.html"
    template_html = template_path.read_text(encoding="utf-8")

    cover_path = "images/cover.jpg"
    alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

    body_html = template_html.replace("{{ cover_src }}", cover_path)
    body_html = body_html.replace("{{ alt_text }}", alt_text)

    return body_html
