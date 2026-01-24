from pathlib import Path

from src.generate.process.audio.main import process_audio


def test_process_audio_calls_implementation(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    wav_source = project_root / "tests" / "test_data" / "track_mix.wav"

    repo_root = tmp_path
    track_dir = repo_root / "music" / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    wav = track_dir / "song_mix.wav"
    wav.write_bytes(wav_source.read_bytes())

    url = "test-track"

    process_audio(track_dir=track_dir, repo_root=repo_root, url=url)

    mp3_dest = repo_root / "src" / "web" / "tracks" / url / "audio" / "track.mp3"

    assert mp3_dest.exists()
