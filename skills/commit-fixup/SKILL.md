---
name: commit-fixup
description: Fixup or amend an existing git commit.
---

Execute each section sequentially. Do not parallelize across sections.

## Staging review

1. Run `git status` to verify what is currently staged. If anything staged is not intended for this commit, run `git reset` to unstage it.
2. Run `git add` on the files relevant to this commit.
3. Run `git diff --cached` to review all staged changes and verify that every change belongs in this commit. If anything irrelevant is staged, stop and tell the user.

## Find target commit

1. Run `git log --oneline -20`.
2. Show the user the commit hash and subject line. If it is the last commit, mention that `--amend` will be used. Ask the user to confirm.

## Determine message update

1. Run `git log -1 --format=%B <hash>` to read the existing commit message.
2. If the staged changes are within its scope, keep the message.
3. Otherwise, read the full commit diff with `git diff <hash>~1 <hash>`, combine with the staged changes, and rewrite the message following the commit message rules.

## Apply changes

Branch based on the target commit and whether the message needs updating:

- **Last commit, keep message:** `git commit --amend --no-edit`
- **Last commit, update message:** `git commit --amend` with the new message
- **Older commit, keep message:** `git commit --fixup=<hash>`, then `GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash <hash>~1`
- **Older commit, update message:** `git commit --fixup=amend:<hash>` with the new message, then `GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash <hash>~1`
