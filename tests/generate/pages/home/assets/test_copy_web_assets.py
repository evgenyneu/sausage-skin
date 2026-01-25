from pathlib import Path

from src.generate.pages.home.assets import copy_web_assets


def test_copy_web_assets_copies_css(tmp_path: Path) -> None:
    repo_root = tmp_path

    src_css = repo_root / "src" / "web" / "css" / "app.css"
    src_css.parent.mkdir(parents=True, exist_ok=True)
    src_css.write_text("body { margin: 0; }", encoding="utf-8")

    copy_web_assets(repo_root=repo_root)

    web_css = repo_root / "web" / "css" / "app.css"

    assert web_css.exists()
    assert web_css.read_text(encoding="utf-8") == "body { margin: 0; }"


def test_copy_web_assets_copies_js(tmp_path: Path) -> None:
    repo_root = tmp_path

    src_js = repo_root / "src" / "web" / "js" / "index.js"
    src_js.parent.mkdir(parents=True, exist_ok=True)
    src_js.write_text("console.log('test');", encoding="utf-8")

    copy_web_assets(repo_root=repo_root)

    web_js = repo_root / "web" / "js" / "index.js"

    assert web_js.exists()
    assert web_js.read_text(encoding="utf-8") == "console.log('test');"


def test_copy_web_assets_removes_existing_css(tmp_path: Path) -> None:
    repo_root = tmp_path

    web_css = repo_root / "web" / "css" / "old.css"
    web_css.parent.mkdir(parents=True, exist_ok=True)
    web_css.write_text("old content", encoding="utf-8")

    src_css = repo_root / "src" / "web" / "css" / "app.css"
    src_css.parent.mkdir(parents=True, exist_ok=True)
    src_css.write_text("new content", encoding="utf-8")

    copy_web_assets(repo_root=repo_root)

    assert not web_css.exists()
    assert (repo_root / "web" / "css" / "app.css").exists()
