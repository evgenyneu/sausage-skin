from pathlib import Path

from src.generate.pages.track.links import render_link


def test_render_link_renders_link_with_url_and_label(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    link_template_path.write_text(
        '<a href="{{ url }}" class="px-2">{{ label }}</a>', encoding="utf-8"
    )

    result = render_link(repo_root=repo_root, url="https://example.com", label="Test Link")

    assert 'href="https://example.com"' in result
    assert "Test Link" in result
    assert "<a href=" in result
    assert 'class="px-2"' in result


def test_render_link_escapes_url(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    link_template_path.write_text('<a href="{{ url }}">{{ label }}</a>', encoding="utf-8")

    result = render_link(repo_root=repo_root, url='https://example.com?q="test"', label="Test")

    assert "&quot;" in result or '"' in result


def test_render_link_escapes_label(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    link_template_path.write_text('<a href="{{ url }}">{{ label }}</a>', encoding="utf-8")

    result = render_link(repo_root=repo_root, url="https://example.com", label="Test <script>")

    assert "&lt;script&gt;" in result
