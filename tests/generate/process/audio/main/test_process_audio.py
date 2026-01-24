from pathlib import Path

from src.generate.process.audio.main import process_audio


def test_process_audio_calls_implementation(tmp_path: Path) -> None:
    repo_root = tmp_path
    track_dir = repo_root / "music" / "a2024" / "a01_jan" / "a01_test"
    track_dir.mkdir(parents=True)

    url = "test-track"

    process_audio(track_dir=track_dir, repo_root=repo_root, url=url)
