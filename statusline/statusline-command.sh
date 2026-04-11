#!/usr/bin/env bash

set -e

# Detect color support
color_supported=0
if [ -z "$NO_COLOR" ] && command -v tput >/dev/null 2>&1 && [ "$(tput colors 2>/dev/null || echo 0)" -ge 8 ]; then
    color_supported=1
fi

# Check python availability
if ! command -v python >/dev/null 2>&1; then
    msg="python command not available"
    if [ "$color_supported" = "1" ]; then
        printf '\033[31m%s\033[0m' "$msg"
    else
        printf '%s' "$msg"
    fi
    exit 0
fi

cd "$(dirname "$0")"

ARGS=()
if [ "$color_supported" = "1" ]; then
    ARGS+=("--color")
fi

python statusline-command.py "${ARGS[@]}"
