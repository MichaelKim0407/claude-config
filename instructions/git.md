# Git

- Always use `git -C <repo>` to specify the repo path explicitly. Do not use bare `git` without `-C`, and do not compound `cd <repo> && git`.
- Never chain `git add`, `git commit`, or `git push` commands. Execute each separately.
- When asked to checkout a branch, always fetch first.

## How to perform a fixup

1. Find the relevant commit with `git log --oneline -- <file>`.
2. Stage the changes.
3. Run `git commit --fixup=<hash>` to create the fixup commit.
4. Run `GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash <hash>~1` to squash it in non-interactively.
