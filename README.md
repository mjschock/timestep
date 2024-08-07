# Timestep AI

Timestep AI CLI - free, local-first, open-source AI

**Development Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install poetry==1.8.3
$ cp .env.example .env
$ direnv allow # See https://direnv.net/#getting-started
$ make
```

**Library Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install timestep
```

**Usage Prerequisites**:

```console
$ prefect server start
$ prefect worker start --pool "default"
```

**Usage**:

```console
$ timestep [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `up`: Start up the Timestep AI platform at...

## `timestep up`

Start up the Timestep AI platform at http://{host}:{port}.

**Usage**:

```console
$ timestep up [OPTIONS]
```

**Options**:

* `--dev TEXT`: [default: False]
* `--host TEXT`: [default: 0.0.0.0]
* `--port TEXT`: [default: 8000]
* `--help`: Show this message and exit.
