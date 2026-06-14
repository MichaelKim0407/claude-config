# IDE

## Diagnostics

The IDE plugin (e.g. PyCharm) automatically shares diagnostics (lint, syntax,
and other inspection messages) as you work. Ignore the following categories
entirely — do not act on them and do not mention them:

- Any diagnostics on markdown files.
- Line-ending diagnostics (e.g. CRLF vs LF), regardless of file type.

Other diagnostics, such as those related to code, may still be addressed as
appropriate.

## Writing files

- When the IDE plugin is connected, create empty files with the Bash tool
  (`touch <file>`); the Write tool fails on empty content.
