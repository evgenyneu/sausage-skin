from pathlib import Path

from src.generate.process.clean import clean_web_dir


def test_clean_web_dir_removes_files(tmp_path: Path) -> None:
    repo_root = tmp_path

    web_dir = repo_root / "web"
    web_file = web_dir / "test.txt"
    web_subdir = web_dir / "subdir"
    web_subfile = web_subdir / "sub.txt"

    web_subdir.mkdir(parents=True, exist_ok=True)
    web_file.write_text("test", encoding="utf-8")
    web_subfile.write_text("sub", encoding="utf-8")

    assert web_dir.exists()
    assert web_file.exists()
    assert web_subfile.exists()

    clean_web_dir(repo_root=repo_root)

    assert not web_dir.exists()


def test_clean_web_dir_no_web_dir(tmp_path: Path) -> None:
    repo_root = tmp_path

    web_dir = repo_root / "web"

    assert not web_dir.exists()

    clean_web_dir(repo_root=repo_root)

    assert not web_dir.exists()
