from pathlib import Path
from datetime import date

from src.generate.pages.track.html import render_html
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_track_html_writes_output(tmp_path: Path) -> None:
    repo_root = tmp_path

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a01_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a01_test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test Track",
            url="test-track",
            description="test description",
        ),
    )

    render_html(track=track, repo_root=repo_root)

    output_path = repo_root / "web" / "test-track" / "index.html"

    assert output_path.exists()

    html = output_path.read_text(encoding="utf-8")

    assert "<html>" in html
    assert "<body>" in html
    assert 'src="images/cover.jpg"' in html
    assert 'alt="Sausage Skin - Test Track"' in html
