"""Timestep file for ensuring the package is executable
as `timestep` and `python -m timestep`
"""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import Callable

from kedro.framework.cli.utils import KedroCliError, load_entry_points
from kedro.framework.project import configure_project


def _find_run_command(package_name: str) -> Callable:  # type: ignore[type-arg]
    try:
        project_cli = importlib.import_module(f"{package_name}.cli")
        # fail gracefully if cli.py does not exist
    except ModuleNotFoundError as exc:
        if f"{package_name}.cli" not in str(exc):
            raise
        plugins = load_entry_points("project")
        run = _find_run_command_in_plugins(plugins) if plugins else None
        if run:
            # use run command from installed plugin if it exists
            return run
        # use run command from the framework project
        from kedro.framework.cli.project import run  # type: ignore[no-redef]

        return run  # type: ignore[return-value]
    # fail badly if cli.py exists, but has no `cli` in it
    if not hasattr(project_cli, "cli"):
        message = f"Cannot load commands from {package_name}.cli"
        raise KedroCliError(message=message)
    return project_cli.run  # type: ignore[no-any-return]


def _find_run_command_in_plugins(plugins: dict) -> Callable:  # type: ignore[type-arg]
    for group in plugins:
        if "run" in group.commands:
            return group.commands["run"]  # type: ignore[no-any-return]
    return None  # type: ignore[return-value]


def main(*args, **kwargs) -> None:  # type: ignore[no-untyped-def]
    package_name = Path(__file__).parent.name
    configure_project(package_name)
    run = _find_run_command(package_name)
    run(*args, **kwargs)


if __name__ == "__main__":
    main()
