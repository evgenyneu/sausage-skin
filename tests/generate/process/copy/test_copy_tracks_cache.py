from pathlib import Path

import pytest

from src.generate.process.copy import copy_tracks_cache


def test_copy_tracks_cache_copies_files(tmp_path: Path) -> None:
    repo_root = tmp_path

    src_tracks = repo_root / "src" / "web" / "tracks" / "test-track"
    src_images = src_tracks / "images"
    src_audio = src_tracks / "audio"

    src_images.mkdir(parents=True, exist_ok=True)
    src_audio.mkdir(parents=True, exist_ok=True)

    cover_file = src_images / "cover.jpg"
    thumb_file = src_images / "cover_600.jpg"
    audio_file = src_audio / "track.mp3"

    cover_file.write_bytes(b"cover-data")
    thumb_file.write_bytes(b"thumb-data")
    audio_file.write_bytes(b"audio-data")

    copy_tracks_cache(repo_root=repo_root)

    web_tracks = repo_root / "web" / "tracks" / "test-track"
    web_cover = web_tracks / "images" / "cover.jpg"
    web_thumb = web_tracks / "images" / "cover_600.jpg"
    web_audio = web_tracks / "audio" / "track.mp3"

    assert web_cover.exists()
    assert web_thumb.exists()
    assert web_audio.exists()

    assert web_cover.read_bytes() == b"cover-data"
    assert web_thumb.read_bytes() == b"thumb-data"
    assert web_audio.read_bytes() == b"audio-data"


def test_copy_tracks_cache_no_source_dir(tmp_path: Path) -> None:
    from src.generate.errors import ProgramError

    repo_root = tmp_path

    with pytest.raises(ProgramError, match="Source tracks directory does not exist"):
        copy_tracks_cache(repo_root=repo_root)
