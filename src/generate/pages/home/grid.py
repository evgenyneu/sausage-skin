from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.process.cover.thumb import THUMBNAIL_SIZES
from src.generate.tracks.models.track_info import TrackInfo


def render_track_grid(*, tracks: list[TrackInfo], repo_root: Path) -> str:
    template_main_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "main.html"
    )
    template_track_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "track.html"
    )

    template_main = template_main_path.read_text(encoding="utf-8")
    template_track = template_track_path.read_text(encoding="utf-8")

    sorted_tracks = sorted(tracks, key=lambda t: t.date, reverse=True)

    items = []

    web_thumb_width = THUMBNAIL_SIZES["small"]

    for track in sorted_tracks:
        url = track.metadata.url
        thumbnail_path = f"{url}/images/cover_{web_thumb_width}.jpg"
        track_url = f"{url}/"

        alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

        track_html = template_track.replace("{{ track_url }}", track_url)
        track_html = track_html.replace("{{ thumbnail_path }}", thumbnail_path)
        track_html = track_html.replace("{{ alt_text }}", alt_text)

        items.append(track_html)

    tracks_html = "".join(items)

    grid_html = template_main.replace("{{ tracks }}", tracks_html)

    return grid_html
