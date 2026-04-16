# Text Editing

## Tools
- Never issue multiple file edit tool calls in parallel. Always do them sequentially.
- When asked to rename a file and edit its content at the same time, perform the move first and then make content changes. This way the user can review the actual changes.

## Markdown
- Escape dollar signs in markdown files (`\$`).
