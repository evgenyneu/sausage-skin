from pathlib import Path
from subprocess import run

from src.generate.process.audio.audio import process_audio as process_audio_impl
from src.generate.process.audio.metadata import AudioMetadata


def test_process_audio_creates_mp3(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    wav_source = project_root / "tests" / "test_data" / "track_mix.wav"
    cover_source = project_root / "tests" / "test_data" / "track_cover.jpg"

    repo_root = tmp_path
    track_dir = repo_root / "music" / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    wav = track_dir / "song_mix.wav"
    wav.write_bytes(wav_source.read_bytes())

    url = "test-track"

    images_dir = repo_root / "src" / "web" / "tracks" / url / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    cover_1200 = images_dir / "cover_1200.jpg"
    cover_1200.write_bytes(cover_source.read_bytes())

    metadata = AudioMetadata(
        artist="sausage skin", title="Test Track", year=2024, album=None, track_number=None
    )

    process_audio_impl(track_dir=track_dir, repo_root=repo_root, url=url, metadata=metadata)

    mp3_dest = repo_root / "src" / "web" / "tracks" / url / "audio" / "track.mp3"

    assert mp3_dest.exists()

    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a:0",
            "-show_entries",
            "stream=codec_name",
            "-of",
            "csv=p=0",
            str(mp3_dest),
        ],
        check=True,
        capture_output=True,
    )

    codec = result.stdout.decode().strip()

    assert codec == "mp3"


def test_process_audio_skips_when_asset_exists(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    wav_source = project_root / "tests" / "test_data" / "track_mix.wav"

    repo_root = tmp_path
    track_dir = repo_root / "music" / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    wav = track_dir / "song_mix.wav"
    wav.write_bytes(wav_source.read_bytes())

    url = "test-track"

    audio_dir = repo_root / "src" / "web" / "tracks" / url / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    mp3_dest = audio_dir / "track.mp3"
    mp3_dest.write_bytes(b"existing-mp3-data")

    metadata = AudioMetadata(
        artist="sausage skin", title="Test Track", year=2024, album=None, track_number=None
    )

    process_audio_impl(track_dir=track_dir, repo_root=repo_root, url=url, metadata=metadata)

    assert mp3_dest.read_bytes() == b"existing-mp3-data"
