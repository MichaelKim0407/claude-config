---
name: commit
description: Create a git commit or fixup an existing one. Use when asked to commit, amend, or fixup changes.
---

Decide which workflow to use based on conversation context:

- **New commit**: the user wants to create a new, standalone commit. Invoke `/commit-new`.
- **Fixup/amend**: the user wants to fold changes into an existing commit. Invoke `/commit-fixup`.
