from pathlib import Path

from src.generate.process.audio.mp3 import build_mp3_command


def test_build_mp3_command(tmp_path: Path) -> None:
    wav = tmp_path / "track.wav"
    mp3 = tmp_path / "track.mp3"

    command = build_mp3_command(wav=wav, mp3=mp3)

    assert command[:3] == ["ffmpeg", "-y", "-i"]
    assert command[3] == str(wav)
    assert command[4] == "-codec:a"
    assert command[5] == "libmp3lame"
    assert command[6] == "-q:a"
    assert command[7] == "0"
    assert command[8] == str(mp3)
