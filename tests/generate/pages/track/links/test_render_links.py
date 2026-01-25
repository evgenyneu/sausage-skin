from datetime import date
from pathlib import Path

from src.generate.pages.track.links import render_links
from src.generate.tracks.models.links import Links
from src.generate.tracks.models.track_info import TrackInfo
from src.generate.tracks.models.track_metadata import TrackMetadata


def test_render_links_returns_empty_when_no_links(tmp_path: Path) -> None:
    repo_root = tmp_path

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(title="Test", url="test", links=None),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert result == ""


def test_render_links_returns_empty_when_all_links_none(tmp_path: Path) -> None:
    repo_root = tmp_path

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test", url="test", links=Links(youtube=None, soundcloud=None, bandcamp=None)
        ),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert result == ""


def test_render_links_renders_youtube_link(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    links_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "links.html"
    )

    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    links_template_path.parent.mkdir(parents=True, exist_ok=True)

    link_template_path.write_text(
        '<a href="{{ url }}" class="px-2">{{ label }}</a>', encoding="utf-8"
    )
    links_template_path.write_text('<div class="mt-2 px-2">{{ links }}</div>', encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test",
            url="test",
            links=Links(youtube="https://youtube.com/watch?v=123", soundcloud=None, bandcamp=None),
        ),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert "YouTube" in result
    assert "https://youtube.com/watch?v=123" in result
    assert '<div class="mt-2 px-2">' in result


def test_render_links_renders_soundcloud_link(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    links_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "links.html"
    )

    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    links_template_path.parent.mkdir(parents=True, exist_ok=True)

    link_template_path.write_text(
        '<a href="{{ url }}" class="px-2">{{ label }}</a>', encoding="utf-8"
    )
    links_template_path.write_text('<div class="mt-2 px-2">{{ links }}</div>', encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test",
            url="test",
            links=Links(youtube=None, soundcloud="https://soundcloud.com/test", bandcamp=None),
        ),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert "SoundCloud" in result
    assert "https://soundcloud.com/test" in result


def test_render_links_renders_bandcamp_link(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    links_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "links.html"
    )

    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    links_template_path.parent.mkdir(parents=True, exist_ok=True)

    link_template_path.write_text(
        '<a href="{{ url }}" class="px-2">{{ label }}</a>', encoding="utf-8"
    )
    links_template_path.write_text('<div class="mt-2 px-2">{{ links }}</div>', encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test",
            url="test",
            links=Links(youtube=None, soundcloud=None, bandcamp="https://bandcamp.com/test"),
        ),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert "Bandcamp" in result
    assert "https://bandcamp.com/test" in result


def test_render_links_renders_all_links(tmp_path: Path) -> None:
    repo_root = tmp_path

    link_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "link.html"
    )
    links_template_path = (
        repo_root / "src" / "generate" / "pages" / "track" / "templates" / "links.html"
    )

    link_template_path.parent.mkdir(parents=True, exist_ok=True)
    links_template_path.parent.mkdir(parents=True, exist_ok=True)

    link_template_path.write_text(
        '<a href="{{ url }}" class="px-2">{{ label }}</a>', encoding="utf-8"
    )
    links_template_path.write_text('<div class="mt-2 px-2">{{ links }}</div>', encoding="utf-8")

    track = TrackInfo(
        track_dir=Path("/music/test"),
        track_yml_path=Path("/music/test/track.yml"),
        date=date(2024, 1, 1),
        metadata=TrackMetadata(
            title="Test",
            url="test",
            links=Links(
                youtube="https://youtube.com/test",
                soundcloud="https://soundcloud.com/test",
                bandcamp="https://bandcamp.com/test",
            ),
        ),
    )

    result = render_links(track=track, repo_root=repo_root)

    assert "YouTube" in result
    assert "SoundCloud" in result
    assert "Bandcamp" in result
    assert "https://youtube.com/test" in result
    assert "https://soundcloud.com/test" in result
    assert "https://bandcamp.com/test" in result
