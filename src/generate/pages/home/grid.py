from src.generate.const import ARTIST_NAME
from src.generate.process.cover.thumb import THUMBNAIL_SIZES
from src.generate.tracks.models.track_info import TrackInfo


def render_track_grid(*, tracks: list[TrackInfo]) -> str:
    sorted_tracks = sorted(tracks, key=lambda t: t.date, reverse=True)

    items = []

    web_thumb_width = THUMBNAIL_SIZES["small"]

    for track in sorted_tracks:
        url = track.metadata.url
        thumbnail_path = f"{url}/images/cover_{web_thumb_width}.jpg"
        track_url = f"{url}/"

        alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

        items.append(
            f'<a href="{track_url}"><img class="TrackGrid-Image" src="{thumbnail_path}" alt="{alt_text}" /></a>'
        )

    return f'<div class="TrackGrid">{"".join(items)}</div>'
