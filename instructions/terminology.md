# Terminology
- "global memory" or "user memory" refers to `~/.claude/CLAUDE.md`
- "global settings" or "user settings" refers to `~/.claude/settings.json`
- "multiple prompts" means the user will provide information split across multiple inputs. Do NOT respond or act (no tool calls, no implementation) until the user sends a message like "go", "proceed", or "done". Do not take any action until that signal is received.
- "link" to a local file means the full absolute path to the file.
  - On Windows, use the Windows path format (e.g., `C:\Users\...`) not the Git Bash format (e.g., `/c/Users/...`).
