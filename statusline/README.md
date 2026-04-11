# Statusline design

This is for Claude Code's statusline. Documentation if you need it: https://code.claude.com/docs/en/statusline

The statusline is installed using the `install` skill in this repo. If there are issues related to installation, check the skill.

## Implementation

- `statusline-command.sh` — bash wrapper. Performs the pre-check and invokes the python script.
- `statusline-command.py` — python implementation.

## Pre-check (bash wrapper)

Check if color is supported in the terminal.

Test if `python` command is available. If not, display "python command not available".
- If color is supported, make it red.

## Output format

Segments are joined with ` | `, in the order listed below. Each segment is omitted when its underlying data is missing.

## Segments

### Working directory

`workspace.current_dir`, shown as-is.

Compare with `workspace.project_dir`.
- If color is supported, display in green if equal, red if unequal.
- If color is not supported, add a ` !` afterwards.

### Model

`model.display_name`, shown as-is.

### Context usage

`ctx:{N}%`, where `{N}` is `context_window.used_percentage` rounded to an integer.

If color is supported, display green if \<50%, yellow if \>=50%.

### Rate limits

Comma-separated list of:

- `5h:{N}% ({remaining})` from `rate_limits.five_hour`
- `7d:{N}% ({remaining})` from `rate_limits.seven_day`

`{N}` is `rate_limits.?.used_percentage` rounded to an integer.
- If color is supported, display green if \<75%, yellow if \>=75% and \<90%, red if \>=90%.

`{remaining}` is the time until `rate_limits.?.resets_at`.
- `?d?h?m`, but omit larger units that are 0. As long as any unit is non-zero, all units after it must be present.
- Show `0m` as fallback.

### Claude version

`Claude {version}`, where `{version}` is `version` from the stdin JSON.
