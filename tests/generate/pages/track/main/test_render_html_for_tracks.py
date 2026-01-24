from pathlib import Path
from datetime import date

from src.generate.pages.track.main import render_html_for_tracks
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_html_for_tracks_generates_all_track_pages(tmp_path: Path) -> None:
    repo_root = tmp_path

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    track1 = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a01_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a01_test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test Track 1",
            url="test-track-1",
            description="test description 1",
        ),
    )

    track2 = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a02_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a02_test/track.yml"),
        date=date(2024, 1, 2),
        metadata=TrackMetadata(
            title="Test Track 2",
            url="test-track-2",
            description="test description 2",
        ),
    )

    render_html_for_tracks(tracks=[track1, track2], repo_root=repo_root)

    output1 = repo_root / "web" / "test-track-1" / "index.html"
    output2 = repo_root / "web" / "test-track-2" / "index.html"

    assert output1.exists()
    assert output2.exists()

    html1 = output1.read_text(encoding="utf-8")
    html2 = output2.read_text(encoding="utf-8")

    assert 'alt="Sausage Skin - Test Track 1"' in html1
    assert 'alt="Sausage Skin - Test Track 2"' in html2


def test_render_html_for_tracks_empty_list(tmp_path: Path) -> None:
    repo_root = tmp_path

    render_html_for_tracks(tracks=[], repo_root=repo_root)

    web_dir = repo_root / "web"
    assert not web_dir.exists() or len(list(web_dir.glob("*/index.html"))) == 0
