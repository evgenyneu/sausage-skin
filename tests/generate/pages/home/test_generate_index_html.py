from pathlib import Path

from src.generate.pages.home import generate_index_html


def test_generate_index_html_writes_output(tmp_path: Path) -> None:
    repo_root = tmp_path

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"

    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    generate_index_html(repo_root=repo_root)

    output_path = repo_root / "web" / "index.html"

    assert (
        output_path.read_text(encoding="utf-8")
        == "<html><body><div>Hello World</div></body></html>"
    )
