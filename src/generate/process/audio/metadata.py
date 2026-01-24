from dataclasses import dataclass


@dataclass
class AudioMetadata:
    artist: str
    title: str
    year: int
    album: str | None = None
    track_number: int | None = None
