"""Generate MAIN.md with imports for all files in instructions/."""
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent  # .claude/skills/sync/sync.py -> repo root
INSTRUCTIONS_DIR = REPO_ROOT / "instructions"
MAIN_MD = REPO_ROOT / "MAIN.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--dry-run", action="store_true", help="print what would be written without modifying MAIN.md")
    args = parser.parse_args()

    files = sorted(INSTRUCTIONS_DIR.glob("*.md"))
    lines = [f"@instructions/{f.name}" for f in files]
    content = "\n".join(lines) + "\n"

    if args.dry_run:
        print(f"Would write {len(lines)} imports to MAIN.md:")
    else:
        MAIN_MD.write_text(content, encoding="utf-8")
        print(f"Written {len(lines)} imports to MAIN.md:")
    print(content, end="")


if __name__ == "__main__":
    main()
