# `timestep`

Timestep AI CLI

**Usage**:

```console
$ timestep [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `llamafile`
* `serve`: Serve
* `test`: Test
* `train`: Train

## `timestep llamafile`

**Usage**:

```console
$ timestep llamafile [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `load`: Load a model
* `unload`: Unload a model by PID

### `timestep llamafile load`

Load a model

**Usage**:

```console
$ timestep llamafile load [OPTIONS]
```

**Options**:

* `--llamafile-path TEXT`: [default: ./models/TinyLlama-1.1B-Chat-v1.0.F16.llamafile]
* `--host TEXT`: [default: 0.0.0.0]
* `--public-path TEXT`: [default: /zip/llama.cpp/server/public]
* `--port TEXT`: [default: 8080]
* `--help`: Show this message and exit.

### `timestep llamafile unload`

Unload a model by PID

**Usage**:

```console
$ timestep llamafile unload [OPTIONS] PID
```

**Arguments**:

* `PID`: [required]

**Options**:

* `--help`: Show this message and exit.

## `timestep serve`

Serve

**Usage**:

```console
$ timestep serve [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `timestep test`

Test

**Usage**:

```console
$ timestep test [OPTIONS]
```

**Options**:

* `--api-key TEXT`: [default: sk-no-key-required]
* `--base-url TEXT`: [default: http://0.0.0.0:8080/v1]
* `--message TEXT`: [default: Count to 10, with a comma between each number and no newlines. E.g., 1, 2, 3, ...]
* `--help`: Show this message and exit.

## `timestep train`

Train

**Usage**:

```console
$ timestep train [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
