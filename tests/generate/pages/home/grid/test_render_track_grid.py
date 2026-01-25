from datetime import date
from pathlib import Path

from src.generate.pages.home.grid import render_track_grid
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_track_grid(tmp_path: Path) -> None:
    repo_root = tmp_path

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

    result = render_track_grid(tracks=[track1, track2], repo_root=repo_root)

    assert "TrackGrid" in result
    assert "test-track-1" in result
    assert "test-track-2" in result
    assert "Test Track 1" in result
    assert "Test Track 2" in result
    assert "Sausage Skin - Test Track 1" in result
    assert "Sausage Skin - Test Track 2" in result
    assert "cover_600.jpg" in result


def test_render_track_grid_sorts_by_date_newest_first(tmp_path: Path) -> None:
    repo_root = tmp_path

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
    track1 = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a01_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a01_test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Older Track",
            url="older-track",
            description="test description",
        ),
    )

    track2 = TrackInfo(
        track_dir=Path("/music/a2024/a01_jan/a02_test"),
        track_yml_path=Path("/music/a2024/a01_jan/a02_test/track.yml"),
        date=date(2024, 1, 2),
        metadata=TrackMetadata(
            title="Newer Track",
            url="newer-track",
            description="test description",
        ),
    )

    result = render_track_grid(tracks=[track1, track2], repo_root=repo_root)

    newer_index = result.find("newer-track")
    older_index = result.find("older-track")

    assert newer_index < older_index
