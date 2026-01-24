from pathlib import Path
from shutil import rmtree


def clean_web_dir(*, repo_root: Path) -> None:
    web_dir = repo_root / "web"

    if web_dir.exists():
        rmtree(web_dir)
