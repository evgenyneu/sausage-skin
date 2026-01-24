from typing import TYPE_CHECKING

from src.generate.const import ARTIST_NAME

if TYPE_CHECKING:
    from src.generate.tracks.models.track_info import TrackInfo


def render_track_body(*, track: "TrackInfo") -> str:
    cover_path = "images/cover.jpg"
    alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

    return f'<img src="{cover_path}" alt="{alt_text}" />'
