# permissions/

Each JSON file in this folder contains a list of `permissions.allow` entries to merge into `~/.claude/settings.json` via the `/install` skill.

## How allow rules work

Rules are evaluated in order: **deny → ask → allow**. The first matching rule wins.

| State | Behavior |
|-------|----------|
| `allow` | Runs without prompting |
| neither (default) | Prompts for approval each time |
| `deny` | Blocked entirely — cannot run even with approval |

## Shell operator awareness

Claude Code is aware of shell operators. An allow rule only matches the base command — redirects, pipes, and chaining always require approval regardless of allow rules.

For example, with `Bash(cat *)` allowed:

| Command | Result |
|---------|--------|
| `cat file.txt` | auto-allowed |
| `cat file.txt > out.txt` | requires approval |
| `cat file.txt \| grep foo` | requires approval |
| `cat file.txt && echo done` | requires approval |

## Pattern matching

- Patterns are glob-based (e.g., `*` is a wildcard).
- Use two entries per command to allow both with and without arguments:
  ```json
  "Bash(git -C * status)",
  "Bash(git -C * status *)"
  ```
- Avoid trailing `*` on subcommand names (e.g., `Bash(git -C * diff*)`) as it would also match unintended subcommands like `difftool`.
