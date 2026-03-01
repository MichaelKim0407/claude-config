"""Merge permissions/allow entries from repo into ~/.claude/settings.json."""
import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent  # .claude/skills/install/ -> repo root
PERMISSIONS_DIR = REPO_ROOT / "permissions"
SETTINGS_PATH = Path.home() / ".claude" / "settings.json"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--dry-run", action="store_true", help="print what would be written without modifying settings.json")
    args = parser.parse_args()

    # Collect all entries from permissions/ json files
    repo_entries = []
    for f in sorted(PERMISSIONS_DIR.glob("*.json")):
        entries = json.loads(f.read_text(encoding="utf-8"))
        repo_entries.extend(entries)

    # Read existing settings
    settings = json.loads(SETTINGS_PATH.read_text(encoding="utf-8")) if SETTINGS_PATH.exists() else {}
    existing = settings.setdefault("permissions", {}).setdefault("allow", [])

    # Merge: add missing entries (exact match)
    added = [e for e in repo_entries if e not in existing]

    if args.dry_run:
        print(f"Would merge {len(added)} new entries into {SETTINGS_PATH}:")
    else:
        existing.extend(added)
        settings["permissions"]["allow"] = sorted(settings["permissions"]["allow"])
        SETTINGS_PATH.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
        print(f"Merged {len(added)} new entries into {SETTINGS_PATH}:")
    for e in added:
        print(f"  {e}")
    if not added:
        print("  (nothing to add)")


if __name__ == "__main__":
    main()
