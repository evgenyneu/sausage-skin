from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.process.cover.thumb import THUMBNAIL_SIZES
from src.generate.template.render import read_template, replace_attribute_tag, replace_text_tag
from src.generate.tracks.models.track_info import TrackInfo


def render_track_grid(*, tracks: list[TrackInfo], repo_root: Path) -> str:
    template_main_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "main.html"
    )
    template_track_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "track.html"
    )

    template_track = read_template(template_path=template_track_path)

    sorted_tracks = sorted(tracks, key=lambda t: t.date, reverse=True)

    items = []

    web_thumb_width = THUMBNAIL_SIZES["small"]

    for track in sorted_tracks:
        url = track.metadata.url
        thumbnail_path = f"{url}/images/cover_{web_thumb_width}.jpg"
        track_url = f"{url}/"
        alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

        track_html = replace_attribute_tag(
            template_html=template_track, tag="track_url", value=track_url, escape=True
        )

        track_html = replace_attribute_tag(
            template_html=track_html, tag="thumbnail_path", value=thumbnail_path, escape=True
        )

        track_html = replace_attribute_tag(
            template_html=track_html, tag="alt_text", value=alt_text, escape=True
        )

        items.append(track_html)

    tracks_html = "".join(items)

    template_main = read_template(template_path=template_main_path)

    grid_html = replace_text_tag(
        template_html=template_main, tag="tracks", value=tracks_html, escape=False
    )

    return grid_html
