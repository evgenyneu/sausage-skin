from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.process.audio.main import process_audio
from src.generate.process.cover.main import process_cover
from src.generate.tracks.models.track_info import TrackInfo


def process_single_track(*, track: TrackInfo, repo_root: Path) -> None:
    process_cover(
        track_dir=track.track_dir,
        repo_root=repo_root,
        url=track.metadata.url,
    )

    process_audio(
        track_dir=track.track_dir,
        repo_root=repo_root,
        url=track.metadata.url,
        artist=ARTIST_NAME,
        title=track.metadata.title,
    )
