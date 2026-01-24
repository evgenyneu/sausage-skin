from pathlib import Path

from src.generate.process.audio.audio import build_audio_output_path


def test_build_audio_output_path(tmp_path: Path) -> None:
    repo_root = tmp_path
    url = "test-track"

    result = build_audio_output_path(repo_root=repo_root, url=url)

    expected = repo_root / "src" / "web" / "tracks" / url / "audio" / "track.mp3"

    assert result == expected
