python_sources(
    name="lib",
)

python_distribution(
    name="dist",
    dependencies=[":lib"],
    provides=python_artifact(name="my-dist", version="0.0.1"),
    # wheel_config_settings={"--global-option": ["--python-tag", "py311"]},
)

pyoxidizer_binary(
    name="bin",
    dependencies=[":dist"],
)
