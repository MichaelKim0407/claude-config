---
name: commit-new
description: Create a new git commit with proper staging review and message formatting.
---

1. Run `git status` to see what is staged and unstaged. Run `git diff` and/or `git diff --cached` as needed to cover all working-directory changes. If the changes span multiple concerns, propose a split into separate commits and let the user review before proceeding.
2. If anything currently staged is not part of this commit's scope, run `git reset` to unstage it.
3. Run `git add` on the files relevant to this commit.
4. Run `git diff --cached` to review all staged changes and verify that every change belongs in this commit. If anything irrelevant is staged, stop and tell the user.
5. Write the commit message based on the diff from step 4, following the commit message rules.
