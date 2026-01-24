from src.generate.process.thumb import generate_thumbnail_for_track
from src.generate.tracks.models.track_info import TrackInfo


def process_single_track(*, track: TrackInfo) -> None:
    print(f"Processing track {track.track_dir}")

    generate_thumbnail_for_track(track_dir=track.track_dir)
