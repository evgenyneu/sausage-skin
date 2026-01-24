from pathlib import Path

from src.generate.process.audio.mp3 import build_mp3_command


def test_build_mp3_command(tmp_path: Path) -> None:
    wav = tmp_path / "track.wav"
    mp3 = tmp_path / "track.mp3"
    cover = tmp_path / "cover_600.jpg"

    command = build_mp3_command(
        wav=wav, mp3=mp3, artist="sausage skin", title="Test Track", year=2024, cover=cover
    )

    assert command[:3] == ["ffmpeg", "-y", "-i"]
    assert command[3] == str(wav)
    assert command[4] == "-i"
    assert command[5] == str(cover)
    assert command[6] == "-map"
    assert command[7] == "0:a"
    assert command[8] == "-map"
    assert command[9] == "1:v"
    assert command[10] == "-c:v"
    assert command[11] == "copy"
    assert command[12] == "-disposition:v"
    assert command[13] == "attached_pic"
    assert command[14] == "-codec:a"
    assert command[15] == "libmp3lame"
    assert command[16] == "-q:a"
    assert command[17] == "0"
    assert command[18] == "-metadata"
    assert command[19] == "artist=sausage skin"
    assert command[20] == "-metadata"
    assert command[21] == "title=Test Track"
    assert command[22] == "-metadata"
    assert command[23] == "date=2024"
    assert command[24] == str(mp3)
