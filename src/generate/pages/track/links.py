from pathlib import Path

from src.generate.template.render import read_template, replace_attribute_tag, replace_text_tag
from src.generate.tracks.models.track_info import TrackInfo


def render_link(*, repo_root: Path, url: str, label: str) -> str:
    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    link_template = read_template(template_path=link_template_path)

    link_html = replace_attribute_tag(
        template_html=link_template, tag="url", value=url, escape=True
    )
    link_html = replace_text_tag(template_html=link_html, tag="label", value=label, escape=True)

    return link_html


def render_links(*, track: TrackInfo, repo_root: Path) -> str:
    if not track.metadata.links:
        return ""

    links = []

    if track.metadata.links.youtube:
        links.append(
            render_link(repo_root=repo_root, url=track.metadata.links.youtube, label="YouTube")
        )

    if track.metadata.links.soundcloud:
        links.append(
            render_link(
                repo_root=repo_root, url=track.metadata.links.soundcloud, label="SoundCloud"
            )
        )

    if track.metadata.links.bandcamp:
        links.append(
            render_link(repo_root=repo_root, url=track.metadata.links.bandcamp, label="Bandcamp")
        )

    if not links:
        return ""

    links_container_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "links.html"
    )

    links_container_template = read_template(template_path=links_container_template_path)

    links_html = replace_text_tag(
        template_html=links_container_template, tag="links", value=" ".join(links), escape=False
    )

    return links_html
