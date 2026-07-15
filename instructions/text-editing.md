# Text Editing

## Tools
- Never issue multiple file edit tool calls in parallel. Always do them sequentially.
- When asked to rename a file and edit its content at the same time, perform the move first and then make content changes. This way the user can review the actual changes.

## Markdown
- Escape dollar signs in markdown files (`\$`).
- Do NOT hard-wrap markdown. Never insert newlines to keep source lines short — write the content of each element (paragraph, list item, table cell, etc.) as a single source line and let the editor soft-wrap it. This does not affect newlines that separate distinct elements (blank lines between paragraphs, one line per list item, headings, code blocks).
