from datetime import date
from pathlib import Path
from re import match


def extract_date_from_path(track_dir: Path, music_root: Path) -> date:
    relative = track_dir.relative_to(music_root)
    parts = relative.parts

    if len(parts) < 3:
        raise ValueError(f"Invalid track path structure: {relative}")

    year_part = parts[0]
    month_part = parts[1]
    day_part = parts[2]

    year_match = match(r"^a(\d{4})$", year_part)
    month_match = match(r"^a(\d{1,2})_", month_part)
    day_match = match(r"^a(\d{1,2})_", day_part)

    if not year_match or not month_match or not day_match:
        raise ValueError(f"Invalid date format in path: {relative}")

    year = int(year_match.group(1))
    month = int(month_match.group(1))
    day = int(day_match.group(1))

    return date(year, month, day)
