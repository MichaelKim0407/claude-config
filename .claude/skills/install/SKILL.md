---
name: install
description: Ensures MAIN.md from this repo is imported in ~/.claude/CLAUDE.md. Use when setting up on a new device.
disable-model-invocation: true
allowed-tools: Read, Edit, Write
---

Ensure `~/.claude/CLAUDE.md` imports `MAIN.md` from this repo.

Steps:
1. Read `~/.claude/CLAUDE.md`.
2. Determine the absolute path of this repo. Check whether an import line for this repo's `MAIN.md` is already present. The expected line is:
   ```
   @<absolute-repo-path>/MAIN.md
   ```
3. If it is already present, report that nothing needs to be done.
4. If it is not present, add the import line to `~/.claude/CLAUDE.md`. Place it at the beginning of the file, or grouped with other imports if any exist.
5. Report what was changed.
