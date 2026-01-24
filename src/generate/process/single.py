from pathlib import Path

from src.generate.const import ARTIST_NAME
from src.generate.process.audio.main import process_audio
from src.generate.process.audio.metadata import AudioMetadata
from src.generate.process.cover.main import process_cover
from src.generate.tracks.models.track_info import TrackInfo


def process_single_track(*, track: TrackInfo, repo_root: Path) -> None:
    process_cover(
        track_dir=track.track_dir,
        repo_root=repo_root,
        url=track.metadata.url,
    )

    album_name = track.metadata.album.name if track.metadata.album else None
    track_number = track.metadata.album.track_number if track.metadata.album else None

    metadata = AudioMetadata(
        artist=ARTIST_NAME,
        title=track.metadata.title,
        year=track.date.year,
        album=album_name,
        track_number=track_number,
    )

    process_audio(
        track_dir=track.track_dir,
        repo_root=repo_root,
        url=track.metadata.url,
        metadata=metadata,
    )
