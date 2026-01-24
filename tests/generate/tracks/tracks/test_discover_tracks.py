from datetime import date as date_type
from pathlib import Path

from src.generate.tracks.main import discover_tracks


def test_discover_tracks(tmp_path: Path) -> None:
    music_root = tmp_path / "music"
    music_root.mkdir()

    track_dir = music_root / "a2024" / "a11_nov" / "a05_cloven_hoofed"
    track_dir.mkdir(parents=True)
    (track_dir / "track.yml").write_text(
        'title: "test"\nurl: "test"\ndescription: "test description"'
    )

    no_track_dir = music_root / "a2024" / "a11_nov" / "a06_no_track"
    no_track_dir.mkdir(parents=True)

    tracks = discover_tracks(music_root=music_root)

    assert len(tracks) == 1
    assert tracks[0].track_dir == track_dir
    assert tracks[0].track_yml_path == track_dir / "track.yml"
    assert tracks[0].date == date_type(2024, 11, 5)
    assert tracks[0].metadata.title == "test"
