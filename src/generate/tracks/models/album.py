from dataclasses import dataclass


@dataclass
class Album:
    track_number: int | None = None
    name: str | None = None
