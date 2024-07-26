#!/usr/bin/env bash
set -ex

pkg upgrade

pkg install binutils-is-llvm build-essential cmake libopenblas libandroid-execinfo libzmq ninja patchelf python python-pyarrow python-scipy tur-repo

pip3 install cython meson-python packaging pyproject_metadata ruamel.yaml.clib setuptools scikit-build-core versioneer wheel

MATHLIB=m LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir numpy==1.26.4 # 2.0.1

LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir pandas==2.2.2

# LDFLAGS="-lpython3.11" pip3 install --upgrade --no-build-isolation --no-cache-dir --use-deprecated=legacy-resolver pyarrow==17.0.0

# LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir scipy==1.14.0
