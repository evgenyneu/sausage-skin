from pathlib import Path

from src.generate.process.thumb.main import THUMBNAIL_WIDTH, generate_thumbnail_for_track


def test_generate_thumbnail_for_track_uses_cover_and_width(tmp_path: Path, monkeypatch) -> None:
    track_dir = tmp_path / "track"
    track_dir.mkdir()

    cover = track_dir / "song_cover.jpg"
    cover.write_text("data", encoding="utf-8")

    thumbnail = tmp_path / "thumb.jpg"

    calls: dict[str, object] = {}

    def fake_generate_thumbnail(
        *, cover: Path, thumbnail: Path, width: int = THUMBNAIL_WIDTH
    ) -> None:
        calls["cover"] = cover
        calls["thumbnail"] = thumbnail
        calls["width"] = width

    # Patch only the generate_thumbnail helper; find_cover_image still runs real code
    from src.generate.process.thumb import main as thumb_main

    monkeypatch.setattr(thumb_main, "generate_thumbnail", fake_generate_thumbnail)

    generate_thumbnail_for_track(track_dir=track_dir, thumbnail=thumbnail)

    assert calls["cover"] == cover
    assert calls["thumbnail"] == thumbnail
    assert calls["width"] == THUMBNAIL_WIDTH
