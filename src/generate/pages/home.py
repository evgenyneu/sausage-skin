from pathlib import Path
from shutil import copy2

from src.generate.const import ARTIST_NAME
from src.generate.tracks.models.track_info import TrackInfo


def render_track_grid(*, tracks: list[TrackInfo]) -> str:
    sorted_tracks = sorted(tracks, key=lambda t: t.date, reverse=True)

    items = []

    for track in sorted_tracks:
        url = track.metadata.url
        thumbnail_path = f"{url}/images/cover_600.jpg"
        track_url = f"{url}/"

        alt_text = f"{ARTIST_NAME} - {track.metadata.title}"

        items.append(
            f'<a href="{track_url}"><img class="TrackGrid-Image" src="{thumbnail_path}" alt="{alt_text}" /></a>'
        )

    return f'<div class="TrackGrid">{"".join(items)}</div>'


def copy_web_assets(*, repo_root: Path) -> None:
    src_css = repo_root / "src" / "web" / "css"
    src_js = repo_root / "src" / "web" / "js"

    web_css = repo_root / "web" / "css"
    web_js = repo_root / "web" / "js"

    if src_css.exists():
        from shutil import copytree

        if web_css.exists():
            import shutil

            shutil.rmtree(web_css)

        copytree(src_css, web_css)

    if src_js.exists():
        web_js.mkdir(parents=True, exist_ok=True)

        for js_file in src_js.glob("*.js"):
            copy2(js_file, web_js / js_file.name)


def render_html(*, tracks: list[TrackInfo], repo_root: Path) -> None:
    layout_path = repo_root / "src" / "web" / "layout" / "index.html"
    output_path = repo_root / "web" / "index.html"

    layout_html = layout_path.read_text(encoding="utf-8")

    body_html = render_track_grid(tracks=tracks)

    index_html = layout_html.replace("{{ body }}", body_html)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(index_html, encoding="utf-8")

    copy_web_assets(repo_root=repo_root)
