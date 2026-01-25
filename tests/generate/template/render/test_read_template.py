from pathlib import Path

from src.generate.template.render import read_template


def test_read_template_reads_file_content(tmp_path: Path) -> None:
    template_path = tmp_path / "template.html"
    template_path.write_text("Hello World", encoding="utf-8")

    result = read_template(template_path=template_path)

    assert result == "Hello World"


def test_read_template_reads_multiline_content(tmp_path: Path) -> None:
    template_path = tmp_path / "template.html"
    content = "<div>\n  <p>Hello</p>\n</div>"
    template_path.write_text(content, encoding="utf-8")

    result = read_template(template_path=template_path)

    assert result == content
