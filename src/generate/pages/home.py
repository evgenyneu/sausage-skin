from pathlib import Path


def render_html(*, repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / "index.html"

    layout_html = layout_path.read_text(encoding="utf-8")

    index_html = layout_html.replace("{{ body }}", "<div>Hello World</div>")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(index_html, encoding="utf-8")
