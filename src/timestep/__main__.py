"""Timestep file for ensuring the package is executable
as `timestep` and `python -m timestep`
"""

from __future__ import annotations

import importlib
from pathlib import Path

from kedro.framework.cli.utils import KedroCliError, load_entry_points
from kedro.framework.project import configure_project


def _find_run_command(package_name):  # type: ignore[no-untyped-def]
    try:
        project_cli = importlib.import_module(f"{package_name}.cli")
        # fail gracefully if cli.py does not exist
    except ModuleNotFoundError as exc:
        if f"{package_name}.cli" not in str(exc):
            raise
        plugins = load_entry_points("project")
        run = _find_run_command_in_plugins(plugins) if plugins else None  # type: ignore[no-untyped-call]
        if run:
            # use run command from installed plugin if it exists
            return run
        # use run command from `kedro.framework.cli.project`
        from kedro.framework.cli.project import run  # type: ignore[no-redef]

        return run
    # fail badly if cli.py exists, but has no `cli` in it
    if not hasattr(project_cli, "cli"):
        msg = f"Cannot load commands from {package_name}.cli"
        raise KedroCliError(msg)
    return project_cli.run


def _find_run_command_in_plugins(plugins):  # type: ignore[no-untyped-def]
    for group in plugins:
        if "run" in group.commands:
            return group.commands["run"]
    return None


def main(*args, **kwargs):  # type: ignore[no-untyped-def]
    package_name = Path(__file__).parent.name
    configure_project(package_name)
    run = _find_run_command(package_name)  # type: ignore[no-untyped-call]
    run(*args, **kwargs)


if __name__ == "__main__":
    main()  # type: ignore[no-untyped-call]
