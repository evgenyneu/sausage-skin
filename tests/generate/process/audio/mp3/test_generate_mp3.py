from pathlib import Path
from subprocess import run

from src.generate.process.audio.mp3 import generate_mp3


def test_generate_mp3_creates_file(tmp_path: Path) -> None:
    project_root = Path(__file__).resolve().parents[5]
    wav_source = project_root / "tests" / "test_data" / "track_mix.wav"

    wav = tmp_path / "track.wav"
    wav.write_bytes(wav_source.read_bytes())

    mp3 = tmp_path / "track.mp3"

    generate_mp3(wav=wav, mp3=mp3)

    assert mp3.exists()

    codec_result = run(
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
            str(mp3),
        ],
        check=True,
        capture_output=True,
    )

    codec = codec_result.stdout.decode().strip()

    assert codec == "mp3"

    wav_duration_result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0",
            str(wav),
        ],
        check=True,
        capture_output=True,
    )

    mp3_duration_result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0",
            str(mp3),
        ],
        check=True,
        capture_output=True,
    )

    wav_duration = float(wav_duration_result.stdout.decode().strip())
    mp3_duration = float(mp3_duration_result.stdout.decode().strip())

    assert abs(mp3_duration - 4.0) < 0.2
    assert abs(wav_duration - 4.0) < 0.2
