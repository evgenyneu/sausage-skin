from pathlib import Path


def require_single_file(*, directory: Path, pattern: str, description: str) -> Path:
    matches = list(directory.glob(pattern))

    if not matches:
        raise ValueError(f"Missing {description} matching '{pattern}' in {directory}")

    if len(matches) > 1:
        raise ValueError(f"Found multiple {description} matching '{pattern}' in {directory}")

    return matches[0]


def validate_track_sources(*, track_dir: Path) -> None:
    require_single_file(
        directory=track_dir,
        pattern="*_mix.wav",
        description="mix wav file",
    )

    require_single_file(
        directory=track_dir,
        pattern="*_cover.jpg",
        description="cover image",
    )
