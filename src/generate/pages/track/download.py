import re
from pathlib import Path

from src.generate.template.render import read_template, replace_attribute_tag


def make_safe_filename(title: str) -> str:
    filename = title.lower()
    filename = re.sub(r"[^a-z0-9\s-]", "", filename)
    filename = re.sub(r"\s+", "-", filename)
    filename = filename.strip("-")
    return f"{filename}.mp3"


def render_download_link(*, repo_root: Path, track_title: str) -> str:
    download_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "download.html"
    )

    template_html = read_template(template_path=download_template_path)

    filename = make_safe_filename(track_title)

    template_html = replace_attribute_tag(
        template_html=template_html, tag="filename", value=filename, escape=True
    )

    return template_html
