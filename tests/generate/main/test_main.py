from pathlib import Path

from src.generate.main import main


def test_main_runs_pipeline(tmp_path: Path) -> None:
    repo_root = tmp_path
    music_root = repo_root / "music"
    music_root.mkdir()

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

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

    src_tracks = repo_root / "src" / "web" / "tracks"
    src_tracks.mkdir(parents=True, exist_ok=True)

    exit_code = main(repo_root=repo_root, music_root=music_root)

    output_path = repo_root / "web" / "index.html"

    assert output_path.exists()

    index_html = output_path.read_text(encoding="utf-8")

    assert "TrackGrid" in index_html
    assert exit_code == 0
