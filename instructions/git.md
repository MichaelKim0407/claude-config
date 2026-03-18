# Git

- Always use `git -C <repo>` to specify the repo path explicitly. Do not use bare `git` without `-C`, and do not compound `cd <repo> && git`.
- Never chain `git add`, `git commit`, or `git push` commands. Execute each separately.
- When asked to checkout a branch, always fetch first.

## Atomic commits

Each commit should be logically self-contained. When working on a task, always consider which commit a new file or change belongs to — especially when pivoting mid-task or when a new prerequisite is identified.

A file belongs in the commit whose purpose it serves, not necessarily the one currently being built. When committing, pick only the files related to the current commit's purpose — stage selectively if local changes span multiple concerns. Use amend or fixups to place changes into the right commit retroactively.

## Making a commit

1. Run `git status` to verify what is currently staged. If anything staged is not intended for this commit, run `git reset` to unstage it.
2. Run `git add` on the files relevant to this commit.
3. Run `git diff --cached` to review all staged changes and verify that every change belongs in this commit. If anything irrelevant is staged, stop and tell the user.
4. Write the commit message following the instructions below on how to write a Git commit message:
   - **IMPORTANT**: Base the message on the actual diff, not on what you did in the current session.
   - **New commit:** base the message on the diff from step 3.
   - **Amend/fixup:** run `git log -1 --format=%B <hash>` to read the existing commit message. If the staged changes are within its scope, keep the message. Otherwise, read the full commit diff with `git diff <hash>~1 <hash>`, combine with the staged changes, and rewrite the message following the rules below.

### [How to Write a Git Commit Message](https://cbea.ms/git-commit/)

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line (e.g. "Fix bug", not "Fixed bug")
- Wrap the body at 72 characters
- Use the body to explain what and why, not how

## How to perform a fixup

1. Find the relevant commit with `git log --oneline -- <file>`.
2. Stage the changes.
3. Run `git commit --fixup=<hash>` to create the fixup commit.
4. Run `GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash <hash>~1` to squash it in non-interactively.
