"""Update ~/.claude/settings.json and install supporting files."""
import argparse
import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent  # .claude/skills/install/ -> repo root
PERMISSIONS_DIR = REPO_ROOT / "permissions"
CLAUDE_DIR = Path.home() / ".claude"
SETTINGS_PATH = CLAUDE_DIR / "settings.json"


def to_bash_path(p: Path) -> str:
    """Converts windows path to Git Bash path.

    e.g. C:/Users/foo/.claude/statusline-command.sh
      -> /c/Users/foo/.claude/statusline-command.sh
    """
    if sys.platform == "win32":
        drive = p.drive.rstrip(':').lower()
        return "/".join(["", drive, *p.parts[1:]])
    return str(p)


class StatuslineInstaller:
    SRC_DIR = REPO_ROOT / "statusline"
    DEST_DIR = CLAUDE_DIR
    FILES = (
        "statusline-command.sh",
        "statusline-command.py",
    )
    SH_DEST = DEST_DIR / "statusline-command.sh"

    def __init__(self, dry_run: bool, settings: dict):
        self.dry_run = dry_run
        self.settings = settings

    def __call__(self) -> bool:
        self.install_scripts()
        return self.configure_setting()

    def install_scripts(self) -> None:
        missing = [f for f in self.FILES if not (self.DEST_DIR / f).exists()]
        if not missing:
            print("Statusline scripts: already present, skipping")
            return
        for f in missing:
            dest = self.DEST_DIR / f
            print(f"Statusline scripts: copying {f} to {dest}")
            if not self.dry_run:
                shutil.copy(self.SRC_DIR / f, dest)

    def configure_setting(self) -> bool:
        if "statusLine" in self.settings:
            print("statusLine setting: already configured, skipping")
            return False

        config = {"type": "command", "command": f"bash {to_bash_path(self.SH_DEST)}"}
        print(f"statusLine setting: {config}")
        if self.dry_run:
            return False

        self.settings["statusLine"] = config
        return True


class Installer:
    def __init__(self, dry_run: bool):
        self.dry_run = dry_run
        self.settings = json.loads(SETTINGS_PATH.read_text(encoding="utf-8")) if SETTINGS_PATH.exists() else {}
        self.settings_changed = False

    def __call__(self):
        self.merge_permissions()
        self.install_statusline()
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

    def install_statusline(self):
        installer = StatuslineInstaller(self.dry_run, self.settings)
        if installer():
            self.settings_changed = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="print what would change without modifying any files")
    args = parser.parse_args()
    Installer(dry_run=args.dry_run)()


if __name__ == "__main__":
    main()
