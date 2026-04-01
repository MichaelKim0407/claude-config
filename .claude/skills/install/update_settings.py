"""Update ~/.claude/settings.json and install supporting files."""
import argparse
import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent  # .claude/skills/install/ -> repo root
PERMISSIONS_DIR = REPO_ROOT / "permissions"
STATUSLINE_SRC = REPO_ROOT / "statusline" / "statusline-command.sh"
CLAUDE_DIR = Path.home() / ".claude"
SETTINGS_PATH = CLAUDE_DIR / "settings.json"
STATUSLINE_DEST = CLAUDE_DIR / "statusline-command.sh"


def to_bash_path(p: Path) -> str:
    """Converts windows path to Git Bash path.

    e.g. C:/Users/foo/.claude/statusline-command.sh
      -> /c/Users/foo/.claude/statusline-command.sh
    """
    if sys.platform == "win32":
        drive = p.drive.rstrip(':').lower()
        return "/".join(["", drive, *p.parts[1:]])
    return str(p)


class Installer:
    def __init__(self, dry_run: bool):
        self.dry_run = dry_run
        self.settings = json.loads(SETTINGS_PATH.read_text(encoding="utf-8")) if SETTINGS_PATH.exists() else {}
        self.settings_changed = False

    def __call__(self):
        self.merge_permissions()
        self.install_statusline_script()
        self.configure_statusline_setting()
        if self.settings_changed:
            SETTINGS_PATH.write_text(json.dumps(self.settings, indent=2) + "\n", encoding="utf-8")

    def merge_permissions(self):
        repo_entries = []
        for f in sorted(PERMISSIONS_DIR.glob("*.json")):
            repo_entries.extend(json.loads(f.read_text(encoding="utf-8")))

        existing = self.settings.setdefault("permissions", {}).setdefault("allow", [])
        added = [e for e in repo_entries if e not in existing]
        if not added:
            print("Permissions: nothing to add")
            return

        print(f"Permissions: adding {len(added)} new entries:")
        for e in added:
            print(f"  + {e}")
        if self.dry_run:
            return

        existing.extend(added)
        self.settings["permissions"]["allow"] = sorted(existing)
        self.settings_changed = True

    def install_statusline_script(self):
        if STATUSLINE_DEST.exists():
            print("Statusline script: already present, skipping")
            return

        print(f"Statusline script: copying to {STATUSLINE_DEST}")
        if self.dry_run:
            return

        shutil.copy(STATUSLINE_SRC, STATUSLINE_DEST)

    def configure_statusline_setting(self):
        if "statusLine" in self.settings:
            print("statusLine setting: already configured, skipping")
            return

        config = {"type": "command", "command": f"bash {to_bash_path(STATUSLINE_DEST)}"}
        print(f"statusLine setting: {config}")
        if self.dry_run:
            return

        self.settings["statusLine"] = config
        self.settings_changed = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="print what would change without modifying any files")
    args = parser.parse_args()
    Installer(dry_run=args.dry_run)()


if __name__ == "__main__":
    main()
