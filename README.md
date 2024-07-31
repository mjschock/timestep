# Timestep AI

**Usage**:

```console
$ timestep [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `load`: Load a model
* `unload`: Unload a model by PID

## `timestep load`

Load a model

**Usage**:

```console
$ timestep load [OPTIONS]
```

**Options**:

* `--llamafile-path TEXT`: [default: ./models/TinyLlama-1.1B-Chat-v1.0.F16.llamafile]
* `--host TEXT`: [default: 0.0.0.0]
* `--port TEXT`: [default: 8080]
* `--help`: Show this message and exit.

## `timestep unload`

Unload a model by PID

**Usage**:

```console
$ timestep unload [OPTIONS] PID
```

**Arguments**:

* `PID`: [required]

**Options**:

* `--help`: Show this message and exit.
