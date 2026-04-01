#!/usr/bin/env bash
python -c '
import sys, json

d = json.load(sys.stdin)

parts = []

cwd = d.get("cwd") or (d.get("workspace") or {}).get("current_dir") or ""
if cwd:
    parts.append(cwd)

model = (d.get("model") or {}).get("display_name") or ""
if model:
    parts.append(model)

ctx = d.get("context_window") or {}
used = ctx.get("used_percentage")
if used is not None:
    parts.append(f"ctx:{round(used)}%")

rl = d.get("rate_limits") or {}
five = (rl.get("five_hour") or {}).get("used_percentage")
week = (rl.get("seven_day") or {}).get("used_percentage")
rate_parts = []
if five is not None:
    rate_parts.append(f"5h:{round(five)}%")
if week is not None:
    rate_parts.append(f"7d:{round(week)}%")
if rate_parts:
    parts.append(" ".join(rate_parts))

print(" | ".join(parts), end="")
'
