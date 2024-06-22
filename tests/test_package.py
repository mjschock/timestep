from __future__ import annotations

import importlib.metadata

import timestep as m


def test_version():
    assert importlib.metadata.version("timestep") == m.__version__
