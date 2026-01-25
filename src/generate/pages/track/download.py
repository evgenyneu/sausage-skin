from pathlib import Path

from src.generate.template.render import read_template


def render_download_link(*, repo_root: Path) -> str:
    download_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "download.html"
    )

    return read_template(template_path=download_template_path)
