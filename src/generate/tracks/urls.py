from src.generate.tracks.models.track_info import TrackInfo


def ensure_unique_urls(*, tracks: list[TrackInfo]) -> None:
    seen: dict[str, TrackInfo] = {}

    for track in tracks:
        url = track.metadata.url

        if url in seen:
            other = seen[url]

            raise ValueError(
                f"Duplicate url '{url}' for tracks {other.track_dir} and {track.track_dir}"
            )

        seen[url] = track
