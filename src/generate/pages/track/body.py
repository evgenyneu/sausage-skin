from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.template.render import read_template, replace_attribute_tag, replace_text_tag
from src.generate.tracks.models.track_info import TrackInfo
from .download import render_download_link
from .links import render_links


def render_track_body(*, track: "TrackInfo", repo_root: Path) -> str:
    template_path = repo_root / "src" / "generate" / "pages" / "track" / "templates" / "main.html"
    template_html = read_template(template_path=template_path)

    cover_path = "images/cover.jpg"
    alt_text = f"{ARTIST_NAME} - {track.metadata.title}"
    description_text = track.metadata.description or ""
    download_link_html = render_download_link(repo_root=repo_root, track_title=track.metadata.title)
    links_html = render_links(track=track, repo_root=repo_root)

    template_html = replace_attribute_tag(
        template_html=template_html, tag="cover_src", value=cover_path, escape=True
    )

    template_html = replace_attribute_tag(
        template_html=template_html, tag="alt_text", value=alt_text, escape=True
    )

    template_html = replace_text_tag(
        template_html=template_html, tag="description", value=description_text, escape=True
    )

    template_html = replace_text_tag(
        template_html=template_html, tag="download_link", value=download_link_html, escape=False
    )

    template_html = replace_text_tag(
        template_html=template_html, tag="links", value=links_html, escape=False
    )

    return template_html
