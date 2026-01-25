from pathlib import Path

from src.generate.pages.track.download import render_download_link


def test_render_download_link_reads_template(tmp_path: Path) -> None:
    repo_root = tmp_path

    download_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "download.html"
    )
    download_template_path.parent.mkdir(parents=True, exist_ok=True)
    download_template_path.write_text(
        '<div><a href="audio/track.mp3" download>Download MP3</a></div>', encoding="utf-8"
    )

    result = render_download_link(repo_root=repo_root)

    assert "<div>" in result
    assert '<a href="audio/track.mp3"' in result
    assert "download" in result
    assert "Download MP3" in result


def test_render_download_link_returns_exact_template_content(tmp_path: Path) -> None:
    repo_root = tmp_path

    template_content = '<div class="mt-2 px-2 text-center">\n    <a href="audio/track.mp3" download class="px-2">Download MP3</a>\n</div>\n'

    download_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "download.html"
    )

    download_template_path.parent.mkdir(parents=True, exist_ok=True)
    download_template_path.write_text(template_content, encoding="utf-8")

    result = render_download_link(repo_root=repo_root)

    assert result == template_content
