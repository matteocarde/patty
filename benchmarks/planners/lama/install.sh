#!/bin/bash

MAINDIR=$PWD
INSTALL_DIR=$PWD/lama-planner

# Cleanup previous install
rm -rf  $INSTALL_DIR build base-cmake

# Get, compile, and install CMAKE Rock share libs
git clone https://github.com/rock-core/base-cmake.git base-cmake
cd base-cmake
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR ..
make install
export Rock_DIR=$INSTALL_DIR/share/rock/cmake/

# compile & install LAMA
cd $MAINDIR
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR ..
make install

echo
echo "LAMA planner installed in folder $INSTALL_DIR"

