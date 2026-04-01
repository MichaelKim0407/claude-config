---
name: install
description: Ensures MAIN.md from this repo is imported in ~/.claude/CLAUDE.md, and merges repo permissions into ~/.claude/settings.json. Use when setting up on a new device.
disable-model-invocation: true
allowed-tools: Read, Edit, Write, Bash(python *)
---

Ensure `~/.claude/CLAUDE.md` imports `MAIN.md` from this repo, and update `~/.claude/settings.json` and supporting files.

## Task 1: CLAUDE.md import

1. Read `~/.claude/CLAUDE.md`.
2. Determine the absolute path of this repo. Check whether an import line for this repo's `MAIN.md` is already present. The expected line is:
   ```
   @<absolute-repo-path>/MAIN.md
   ```
3. If it is already present, report that nothing needs to be done for this task.
4. If it is not present, add the import line to `~/.claude/CLAUDE.md`. Place it at the beginning of the file, or grouped with other imports if any exist.
5. Report what was changed.

## Task 2: update settings

1. Run `update_settings.py` from this repo:
   ```
   python <absolute-repo-path>/.claude/skills/install/update_settings.py
   ```
   This script handles three things:
   - Merges `permissions/allow` entries into `~/.claude/settings.json`
   - Copies `statusline/statusline-command.sh` to `~/.claude/` (skips if already present)
   - Adds the `statusLine` key to `~/.claude/settings.json` (skips if already present)
2. Report what was changed.
