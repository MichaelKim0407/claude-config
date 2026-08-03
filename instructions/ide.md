# IDE

## Diagnostics

The IDE plugin (e.g. PyCharm) automatically shares diagnostics (lint, syntax, and other inspection messages) as you work. Ignore the following categories entirely — do not act on them and do not mention them:

- Any diagnostics on markdown files.
- Line-ending diagnostics (e.g. CRLF vs LF), regardless of file type.

Other diagnostics, such as those related to code, may still be addressed as appropriate.

## Writing files

- When the IDE plugin is connected, and the intended file content is empty, create the file with the Bash tool (`touch <file>`); the Write tool fails on empty content.
- When an Edit or Write result is flagged that the user modified the proposed content before accepting it, ALWAYS re-read the file immediately.
