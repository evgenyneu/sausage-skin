from pathlib import Path
from subprocess import CalledProcessError, run

from src.generate.errors import ProgramError


def build_mp3_command(*, wav: Path, mp3: Path) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-i",
        str(wav),
        "-codec:a",
        "libmp3lame",
        "-q:a",
        "0",
        str(mp3),
    ]


def generate_mp3(*, wav: Path, mp3: Path) -> None:
    command = build_mp3_command(wav=wav, mp3=mp3)

    try:
        run(command, check=True, capture_output=True)
    except CalledProcessError as error:
        stderr = error.stderr.decode(errors="ignore") if error.stderr else ""
        message = f"Failed to generate MP3 for {wav}: {stderr.strip()}"

        raise ProgramError(message) from error
