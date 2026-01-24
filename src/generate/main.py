from __future__ import annotations

from pathlib import Path


def render_index_html(layout_html: str, body_html: str) -> str:
    return layout_html.replace("{{ body }}", body_html)


def generate_index_html(repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / "index.html"

    layout_html = layout_path.read_text(encoding="utf-8")
    index_html = render_index_html(layout_html=layout_html, body_html="<div>Hello World</div>")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(index_html, encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]

    generate_index_html(repo_root=repo_root)


if __name__ == "__main__":
    main()
