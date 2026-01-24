from pathlib import Path
from .index_html import generate_index_html

def main() -> None:
    repo_root = Path.cwd()

    generate_index_html(repo_root=repo_root)


if __name__ == "__main__":
    main()
