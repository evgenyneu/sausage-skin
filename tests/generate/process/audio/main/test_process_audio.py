from pathlib import Path

from src.generate.process.audio.main import process_audio
from src.generate.process.audio.metadata import AudioMetadata


def test_process_audio_calls_implementation(tmp_path: Path) -> None:
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

    cover_600 = images_dir / "cover_600.jpg"
    cover_600.write_bytes(cover_source.read_bytes())

    metadata = AudioMetadata(
        artist="sausage skin", title="Test Track", year=2024, album=None, track_number=None
    )

    process_audio(track_dir=track_dir, repo_root=repo_root, url=url, metadata=metadata)

    mp3_dest = repo_root / "src" / "web" / "tracks" / url / "audio" / "track.mp3"

    assert mp3_dest.exists()
