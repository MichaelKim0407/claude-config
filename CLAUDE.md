# claude-config

This repo stores personal Claude instructions shared across devices.

## Structure

- `MAIN.md` — imported into global memory (`~/.claude/CLAUDE.md`). Imports all files under `instructions/`.
- `instructions/` — individual instruction files, each covering a specific topic.
- `.claude/skills/` — project-level skills for managing this repo.

## Import chain

```
~/.claude/CLAUDE.md
  └── @D:/Dev/claude-config/MAIN.md        (hop 1)
        └── @instructions/<file>.md ...    (hop 2)
```

> **Note:** Claude Code supports a maximum import nesting depth of 5 hops. This structure uses 2.

## Skills

- `/sync` — ensures all files under `instructions/` are imported in `MAIN.md`
- `/install` — ensures `MAIN.md` is imported in `~/.claude/CLAUDE.md`

## Working with this repo

- When adding new instructions, find the most appropriate existing file under `instructions/` to add to, or create a new file if nothing fits.
- To add a new instruction file under `instructions/`, run `/sync` to register it in `MAIN.md`.
- After pulling changes on a new device, run `/install` to register with global memory.
