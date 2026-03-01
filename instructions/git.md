# Git

- Always use `git -C <repo>` to specify the repo path explicitly. Do not use bare `git` without `-C`, and do not compound `cd <repo> && git`.
- Never chain `git add`, `git commit`, or `git push` commands. Execute each separately.
- When asked to checkout a branch, always fetch first.

## Atomic commits

Each commit should be logically self-contained. When working on a task, always consider which commit a new file or change belongs to — especially when pivoting mid-task or when a new prerequisite is identified.

A file belongs in the commit whose purpose it serves, not necessarily the one currently being built. When committing, pick only the files related to the current commit's purpose — stage selectively if local changes span multiple concerns. Use amend or fixups to place changes into the right commit retroactively.

## Commit messages

When writing a commit message, base it on the actual diff, not on what you did in the current session.

## How to perform a fixup

1. Find the relevant commit with `git log --oneline -- <file>`.
2. Stage the changes.
3. Run `git commit --fixup=<hash>` to create the fixup commit.
4. Run `GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash <hash>~1` to squash it in non-interactively.
