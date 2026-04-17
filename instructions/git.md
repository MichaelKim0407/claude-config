# Git

- Always use `git -C <repo>` to specify the repo path explicitly. Do not use bare `git` without `-C`, and do not compound `cd <repo> && git`.
- Never chain `git add`, `git commit`, or `git push` commands. Execute each separately.
- When asked to commit changes, use the `/commit` skill.
- When asked to checkout a branch, always fetch first.
- When referencing the `main` or `develop` branch, always use the remote reference (e.g. `origin/main`, `origin/develop`). Never create a local branch for them, and never reference them as local branches.

## Atomic commits

Each commit should be logically self-contained. When working on a task, always consider which commit a new file or change belongs to — especially when pivoting mid-task or when a new prerequisite is identified.

A file belongs in the commit whose purpose it serves, not necessarily the one currently being built. When committing, pick only the files related to the current commit's purpose — stage selectively if local changes span multiple concerns. Use amend or fixups to place changes into the right commit retroactively.

## [How to Write a Git Commit Message](https://cbea.ms/git-commit/)

- **IMPORTANT**: Base the message on the actual diff, not on what you did in the current session
- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line (e.g. "Fix bug", not "Fixed bug")
- Wrap the body at 72 characters
- Use the body to explain what and why, not how
- End the message with a blank line followed by the `Co-Authored-By` trailer specified in the system instructions
