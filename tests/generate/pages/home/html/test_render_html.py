from datetime import date as date_type
from pathlib import Path

from src.generate.pages.home.html import render_html
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_html_writes_output(tmp_path: Path) -> None:
    repo_root = tmp_path

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    css_app = repo_root / "src" / "web" / "css" / "app.css"
    css_base = repo_root / "src" / "web" / "css" / "base" / "main.css"
    css_module = repo_root / "src" / "web" / "css" / "modules" / "track-grid.css"

    css_app.parent.mkdir(parents=True, exist_ok=True)
    css_base.parent.mkdir(parents=True, exist_ok=True)
    css_module.parent.mkdir(parents=True, exist_ok=True)

    css_app.write_text(
        '@import "base/main.css";\n@import "modules/track-grid.css";', encoding="utf-8"
    )
    css_base.write_text("body { margin: 0; }", encoding="utf-8")
    css_module.write_text(".TrackGrid { display: grid; }", encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a01_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a01_test/track.yml"),
        date=date_type(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test Track",
            url="test-track",
            description="test description",
        ),
    )

    render_html(tracks=[track], repo_root=repo_root)

    output_path = repo_root / "web" / "index.html"
    output_html = output_path.read_text(encoding="utf-8")

    assert "TrackGrid" in output_html
    assert "test-track" in output_html
    assert "Test Track" in output_html

    css_output = repo_root / "web" / "css" / "app.css"
    assert css_output.exists()
