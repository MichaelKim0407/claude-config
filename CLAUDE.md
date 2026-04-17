# claude-config

This repo stores personal Claude instructions shared across devices.

## Structure

- `MAIN.md` — imported into global memory (`~/.claude/CLAUDE.md`). Imports all files under `instructions/`.
- `instructions/` — individual instruction files, each covering a specific topic.
- `permissions/` — JSON files, one per topic, each containing a list of `permissions.allow` entries to merge into `~/.claude/settings.json`.
- `skills/` — global skills installed to `~/.claude/skills/` by `/install`.
- `statusline/` — statusline script installed to `~/.claude/` by `/install`.
- `.claude/skills/` — project-level skills for managing this repo.

## Instructions import chain

```
~/.claude/CLAUDE.md
  └── @D:/Dev/claude-config/MAIN.md        (hop 1)
        └── @instructions/<file>.md ...    (hop 2)
```

> **Note:** Claude Code supports a maximum import nesting depth of 5 hops. This structure uses 2.

## Skills

- `/sync` — ensures all files under `instructions/` are imported in `MAIN.md`
- `/install` — ensures `MAIN.md` is imported in `~/.claude/CLAUDE.md`, merges `permissions/` entries into `~/.claude/settings.json`, installs global skills, and installs the statusline script

## Working with this repo

### Updating instructions

- Find the most appropriate existing file under `instructions/` to add to, or create a new file if nothing fits.
- If a new file was created, run `/sync` to register it in `MAIN.md`.
- `instructions/behavior.md` is also loaded into claude.ai web chat. Rules added there should be worded to apply in both environments — avoid Claude Code-specific terminology (tool names, subagents, hooks, etc.) where possible, or scope the rule explicitly when it only applies to one environment.

### Updating permissions

- Add or update a JSON file under `permissions/`. Each file is a list of `permissions.allow` entries.
- Run `/install` to merge the updated entries into `~/.claude/settings.json`.

### Updating skills

- Add or update a skill under `skills/<skill-name>/SKILL.md`.
- Run `/install` to copy skills to `~/.claude/skills/`.

### Updating from remote

- After pulling changes on a new device, run `/install` to register with global memory, sync permissions, and install skills.
