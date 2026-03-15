# Text Editing

## Tools
- Never issue multiple file edit tool calls in parallel. Always do them sequentially.
- Do not use `cat` to read text files. Use the Read tool.
- Do not use unix commands (such as `cat`, `echo`, `sed`) to edit files. Use the Edit or Write tool.
- When asked to rename a file and edit its content at the same time, perform the move first and then make content changes. This way the user can review the actual changes.
