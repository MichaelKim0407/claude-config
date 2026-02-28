---
name: sync
description: Ensures all files under instructions/ are imported in MAIN.md. Use when a new instruction file has been added.
disable-model-invocation: true
allowed-tools: Bash(python *)
---

Run the sync script to regenerate `MAIN.md` with imports for all files under `instructions/`:

```
python .claude/skills/sync/sync.py
```

Report the output.
