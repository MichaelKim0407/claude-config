"""Claude Code statusline."""
import abc
import argparse
import json
import sys
import time
import typing
from functools import cached_property


class ColoredText:
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    RESET = "\033[0m"

    @classmethod
    def render(cls, text: str, color: str) -> str:
        return f"{color}{text}{cls.RESET}"


class StatuslineRenderer:
    def __init__(
        self,
        data: dict,
        *,
        color: bool,
    ):
        self.data = data
        self.color = color

    def _segments(self) -> typing.Iterator['AbstractSegment']:
        yield WorkingDirectorySegment(self.data, color=self.color)
        yield ModelSegment(self.data, color=self.color)
        yield ContextUsageSegment(self.data, color=self.color)
        yield RateLimitsSegment(self.data, color=self.color)
        yield ClaudeVersionSegment(self.data, color=self.color)

    def __str__(self) -> str:
        return " | ".join(str(seg) for seg in self._segments() if seg)


class AbstractSegment(abc.ABC):
    def __init__(
        self,
        data: dict,
        *,
        color: bool,
    ):
        self.data = data
        self.color = color

    @abc.abstractmethod
    def __bool__(self) -> bool:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class WorkingDirectorySegment(AbstractSegment):
    @cached_property
    def _workspace(self) -> dict:
        return self.data.get("workspace", {})

    @cached_property
    def _current_dir(self) -> typing.Optional[str]:
        return self._workspace.get("current_dir")

    @cached_property
    def _project_dir(self) -> typing.Optional[str]:
        return self._workspace.get("project_dir")

    def __bool__(self) -> bool:
        return self._current_dir is not None

    def __str__(self) -> str:
        if self._project_dir is None:
            return self._current_dir

        equal = self._current_dir == self._project_dir
        if self.color:
            color = ColoredText.GREEN if equal else ColoredText.RED
            return ColoredText.render(self._current_dir, color)
        else:
            return self._current_dir if equal else f"{self._current_dir} !"


class ModelSegment(AbstractSegment):
    @cached_property
    def _model(self) -> dict:
        return self.data.get("model", {})

    @cached_property
    def _display_name(self) -> typing.Optional[str]:
        return self._model.get("display_name")

    def __bool__(self) -> bool:
        return self._display_name is not None

    def __str__(self) -> str:
        return self._display_name


class ContextUsageSegment(AbstractSegment):
    @cached_property
    def _context_window(self) -> dict:
        return self.data.get("context_window", {})

    @cached_property
    def _used_percentage(self) -> typing.Optional[float]:
        return self._context_window.get("used_percentage")

    def __bool__(self) -> bool:
        return self._used_percentage is not None

    def __str__(self) -> str:
        text = f"ctx:{self._used_percentage:.0f}%"
        if self.color:
            color = ColoredText.GREEN if self._used_percentage < 50 else ColoredText.YELLOW
            return ColoredText.render(text, color)
        else:
            return text


class RateLimitsSegment(AbstractSegment):
    _ENTRIES = {
        "five_hour": "5h",
        "seven_day": "7d",
    }

    @cached_property
    def _now(self) -> float:
        return time.time()

    @cached_property
    def _rate_limits(self) -> dict:
        return self.data.get("rate_limits", {})

    @cached_property
    def _entries(self) -> list[tuple[str, float, int]]:
        """label, percent, resets_at"""
        result = []
        for key, label in self._ENTRIES.items():
            entry = self._rate_limits.get(key, {})
            percent = entry.get("used_percentage")
            if percent is None:
                continue
            result.append((label, percent, entry.get("resets_at")))
        return result

    def __bool__(self) -> bool:
        return len(self._entries) > 0

    def _format_remaining(self, resets_at: int) -> str:
        if resets_at is None:
            return ""
        secs = int(resets_at - self._now)
        if secs <= 0:
            return "0m"
        days, rem = divmod(secs, 86400)
        hours, rem = divmod(rem, 3600)
        mins = rem // 60
        # Omit leading zero units; once a unit is non-zero, include all trailing
        # units even if they are zero.
        if days:
            return f"{days}d{hours}h{mins}m"
        if hours:
            return f"{hours}h{mins}m"
        if mins:
            return f"{mins}m"
        return "0m"

    @staticmethod
    def _color(percent: float) -> str:
        if percent < 75:
            return ColoredText.GREEN
        elif percent < 90:
            return ColoredText.YELLOW
        else:
            return ColoredText.RED

    def _format_entry(self, label: str, percent: float, resets_at: int) -> str:
        text = f"{label}:{percent:.0f}%"
        rem = self._format_remaining(resets_at)
        if rem:
            text += f" ({rem})"

        if not self.color:
            return text

        return ColoredText.render(text, self._color(percent))

    def __str__(self) -> str:
        return ", ".join(self._format_entry(*entry) for entry in self._entries)


class ClaudeVersionSegment(AbstractSegment):
    @cached_property
    def _version(self) -> typing.Optional[str]:
        return self.data.get("version")

    def __bool__(self) -> bool:
        return self._version is not None

    def __str__(self) -> str:
        return f"Claude {self._version}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--color", action="store_true")
    args = parser.parse_args()

    data = json.load(sys.stdin)
    renderer = StatuslineRenderer(data, color=args.color)
    print(renderer, end="")


if __name__ == "__main__":
    main()
