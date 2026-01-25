from pathlib import Path
from shutil import copy2, copytree, rmtree


def copy_web_assets(*, repo_root: Path) -> None:
    src_css = repo_root / "src" / "web" / "css"
    src_js = repo_root / "src" / "web" / "js"

    web_css = repo_root / "web" / "css"
    web_js = repo_root / "web" / "js"

    if src_css.exists():
        if web_css.exists():
            rmtree(web_css)

        copytree(src_css, web_css)

    if src_js.exists():
        web_js.mkdir(parents=True, exist_ok=True)

        for js_file in src_js.glob("*.js"):
            copy2(js_file, web_js / js_file.name)
