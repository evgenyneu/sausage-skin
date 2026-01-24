from pathlib import Path

from src.generate.tracks.validate import require_single_file
from src.generate.process.cover.thumb import THUMBNAIL_SIZES
from .metadata import AudioMetadata
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


def build_cover_image_path(*, repo_root: Path, url: str) -> Path:
    images_dir = repo_root / "src" / "web" / "tracks" / url / "images"
    mp3_thumb_width = THUMBNAIL_SIZES["cover_1200"]
    return images_dir / f"cover_{mp3_thumb_width}.jpg"


def process_audio(*, track_dir: Path, repo_root: Path, url: str, metadata: AudioMetadata) -> None:
    source_wav = find_mix_wav(track_dir=track_dir)

    mp3_path = build_audio_output_path(repo_root=repo_root, url=url)
    mp3_path.parent.mkdir(parents=True, exist_ok=True)

    if not mp3_path.exists():
        cover_path = build_cover_image_path(repo_root=repo_root, url=url)

        generate_mp3(wav=source_wav, mp3=mp3_path, cover=cover_path, metadata=metadata)
