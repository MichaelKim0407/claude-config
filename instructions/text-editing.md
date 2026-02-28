# Text Editing

## Tools
- Never issue multiple Write tool calls in parallel. Always do them sequentially.
- When making multiple edits to the same file, combine them into a single Write tool call.
- Do not use `cat` to read text files. Use the Read tool.
- Do not use unix commands (such as `cat`, `echo`, `sed`) to edit files. Use the Write tool.
- When asked to rename a file and edit its content at the same time, perform the move first and then use the Write tool to make content changes. This way the user can review the actual changes.

## Formatting
- When editing text files, always keep a newline at the end of file.
