from datetime import date as date_type
from pathlib import Path

from src.generate.pages.home.main import render_html
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_html_calls_implementation(tmp_path: Path) -> None:
    repo_root = tmp_path

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    css_app = repo_root / "src" / "web" / "css" / "app.css"
    css_app.parent.mkdir(parents=True, exist_ok=True)
    css_app.write_text("body { margin: 0; }", encoding="utf-8")

    template_main_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "main.html"
    )

    template_track_path = (
        repo_root / "src" / "generate" / "pages" / "home" / "templates" / "track.html"
    )

    template_main_path.parent.mkdir(parents=True, exist_ok=True)
    template_track_path.parent.mkdir(parents=True, exist_ok=True)

    template_main_path.write_text('<div class="TrackGrid">{{ tracks }}</div>', encoding="utf-8")
    template_track_path.write_text(
        '<a href="{{ track_url }}"><img class="TrackGrid-Image" src="{{ thumbnail_path }}" alt="{{ alt_text }}" /></a>',
        encoding="utf-8",
    )

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

    assert output_path.exists()
