# Tools

Use Claude's dedicated tools instead of these Bash commands:

- `cat` — use Read to view, Write or Edit to modify (heredoc/redirect)
- `head` — use Read with `limit`
- `grep` — use Grep
- `echo` — use Write to create or overwrite, Edit to append (`>>`)
- `sed` — use Edit

Exception: these commands may be used after a pipe (e.g., `some_cmd | grep foo`, `some_cmd | head -n 10`), since the Claude tools cannot consume piped input.
