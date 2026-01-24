from pathlib import Path

from .audio import process_audio as process_audio_impl


def process_audio(*, track_dir: Path, repo_root: Path, url: str, artist: str, title: str) -> None:
    process_audio_impl(
        track_dir=track_dir, repo_root=repo_root, url=url, artist=artist, title=title
    )
