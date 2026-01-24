from src.generate.tracks.models.track_info import TrackInfo


def process_single_track(*, track: TrackInfo) -> None:
    print(f"Processing track {track.track_dir}")
