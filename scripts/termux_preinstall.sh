#!/usr/bin/env bash
set -ex

yes | pkg upgrade

pkg install binutils-is-llvm build-essential cmake libopenblas libandroid-execinfo libzmq ninja patchelf python

pip3 install cython meson-python packaging pyproject_metadata ruamel.yaml.clib setuptools versioneer wheel

MATHLIB=m LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir numpy==1.26.4

LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir pandas

#pip install scikit-build-core
