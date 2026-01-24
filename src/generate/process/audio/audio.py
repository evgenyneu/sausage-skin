from pathlib import Path

from src.generate.tracks.validate import require_single_file

from .mp3 import generate_mp3


def find_mix_wav(*, track_dir: Path) -> Path:
    return require_single_file(
        directory=track_dir,
        pattern="*_mix.wav",
        description="mix wav file",
    )


def build_audio_output_path(*, repo_root: Path, url: str) -> Path:
    audio_dir = repo_root / "src" / "web" / "tracks" / url / "audio"

    mp3_path = audio_dir / "track.mp3"

    return mp3_path


def process_audio(*, track_dir: Path, repo_root: Path, url: str, artist: str, title: str) -> None:
    source_wav = find_mix_wav(track_dir=track_dir)

    mp3_path = build_audio_output_path(repo_root=repo_root, url=url)
    mp3_path.parent.mkdir(parents=True, exist_ok=True)

    if not mp3_path.exists():
        generate_mp3(wav=source_wav, mp3=mp3_path, artist=artist, title=title)
