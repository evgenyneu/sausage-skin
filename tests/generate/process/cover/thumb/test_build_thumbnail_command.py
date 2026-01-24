from pathlib import Path

from src.generate.process.cover.thumb import THUMBNAIL_WIDTH, build_thumbnail_command


def test_build_thumbnail_command_default_width(tmp_path: Path) -> None:
    cover = tmp_path / "cover.jpg"
    thumbnail = tmp_path / "thumb.jpg"

    command = build_thumbnail_command(cover=cover, thumbnail=thumbnail)

    assert command[:3] == ["ffmpeg", "-y", "-i"]
    assert command[3] == str(cover)
    assert command[4] == "-vf"
    assert command[5] == f"scale={THUMBNAIL_WIDTH}:-1"
    assert command[6] == str(thumbnail)


def test_build_thumbnail_command_custom_width(tmp_path: Path) -> None:
    cover = tmp_path / "cover.jpg"
    thumbnail = tmp_path / "thumb.jpg"

    command = build_thumbnail_command(cover=cover, thumbnail=thumbnail, width=200)

    assert command[5] == "scale=200:-1"
