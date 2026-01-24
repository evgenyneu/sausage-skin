from pathlib import Path

from src.generate.process.thumb.main import find_cover_image


def test_find_cover_image_ok(tmp_path: Path) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    cover = track_dir / "song_cover.jpg"
    cover.write_text("data", encoding="utf-8")

    result = find_cover_image(track_dir=track_dir)

    assert result == cover
