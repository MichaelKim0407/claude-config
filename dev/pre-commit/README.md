# Pre-commit hooks

This project manages [pre-commit](https://pre-commit.com/) hooks for the repository.

## Installation

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv run --project dev/pre-commit pre-commit install --config dev/pre-commit/.pre-commit-config.yaml
```

## Manual run

Run all hooks against all tracked files:

```bash
uv run --project dev/pre-commit pre-commit run --all-files --config dev/pre-commit/.pre-commit-config.yaml
```

## Configuration

Hooks are configured in [`.pre-commit-config.yaml`](.pre-commit-config.yaml). See the [pre-commit docs](https://pre-commit.com/#plugins) for available hooks and options.
