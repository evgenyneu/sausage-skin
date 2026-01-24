from pathlib import Path

from src.generate.main import main


def test_main_runs_pipeline(tmp_path: Path) -> None:
    repo_root = tmp_path
    music_root = repo_root / "music"
    music_root.mkdir()

    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    layout_path.parent.mkdir(parents=True, exist_ok=True)
    layout_path.write_text("<html><body>{{ body }}</body></html>", encoding="utf-8")

    exit_code = main(repo_root=repo_root, music_root=music_root)

    output_path = repo_root / "web" / "index.html"

    assert output_path.exists()

    index_html = output_path.read_text(encoding="utf-8")

    assert "TrackGrid" in index_html
    assert exit_code == 0
