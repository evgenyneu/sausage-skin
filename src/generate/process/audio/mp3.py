from pathlib import Path
from subprocess import CalledProcessError, run

from src.generate.errors import ProgramError
from .metadata import AudioMetadata


def build_mp3_command(
    *,
    wav: Path,
    mp3: Path,
    cover: Path,
    metadata: AudioMetadata,
) -> list[str]:
    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(wav),
        "-i",
        str(cover),
        "-map",
        "0:a",
        "-map",
        "1:v",
        "-c:v",
        "copy",
        "-disposition:v",
        "attached_pic",
        "-codec:a",
        "libmp3lame",
        "-q:a",
        "0",
        "-metadata",
        f"artist={metadata.artist}",
        "-metadata",
        f"title={metadata.title}",
        "-metadata",
        f"date={metadata.year}",
    ]

    if metadata.album:
        command.extend(["-metadata", f"album={metadata.album}"])

    if metadata.track_number is not None:
        command.extend(["-metadata", f"track={metadata.track_number}"])

    command.append(str(mp3))

    return command


def generate_mp3(
    *,
    wav: Path,
    mp3: Path,
    cover: Path,
    metadata: AudioMetadata,
) -> None:
    command = build_mp3_command(wav=wav, mp3=mp3, cover=cover, metadata=metadata)

    try:
        run(command, check=True, capture_output=True)
    except CalledProcessError as error:
        stderr = error.stderr.decode(errors="ignore") if error.stderr else ""
        message = f"Failed to generate MP3 for {wav}: {stderr.strip()}"

        raise ProgramError(message) from error
