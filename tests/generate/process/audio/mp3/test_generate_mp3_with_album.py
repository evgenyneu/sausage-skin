import json
from pathlib import Path
from subprocess import run

from src.generate.process.audio.metadata import AudioMetadata
from src.generate.process.audio.mp3 import generate_mp3
from src.generate.process.cover.thumb import generate_thumbnail


def test_generate_mp3_with_album_tag(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    wav_source = project_root / "tests" / "test_data" / "track_mix.wav"
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    wav = tmp_path / "track.wav"
    wav.write_bytes(wav_source.read_bytes())

    cover_full = tmp_path / "cover_full.jpg"
    cover_full.write_bytes(cover_source.read_bytes())

    cover = tmp_path / "cover_1200.jpg"
    generate_thumbnail(cover=cover_full, thumbnail=cover, width=1200)

    mp3 = tmp_path / "track.mp3"

    metadata = AudioMetadata(
        artist="sausage skin", title="Test Track", year=2024, album="Test Album", track_number=1
    )

    generate_mp3(wav=wav, mp3=mp3, cover=cover, metadata=metadata)

    assert mp3.exists()

    metadata_result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_format",
            "-show_streams",
            "-of",
            "json",
            str(mp3),
        ],
        check=True,
        capture_output=True,
    )

    metadata_json = json.loads(metadata_result.stdout.decode())
    format_tags = metadata_json["format"]["tags"]

    assert format_tags.get("artist") == "sausage skin"
    assert format_tags.get("title") == "Test Track"
    assert format_tags.get("date") == "2024"
    assert format_tags.get("album") == "Test Album"
    assert format_tags.get("track") == "1"
