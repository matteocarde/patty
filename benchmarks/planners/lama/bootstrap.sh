#!/bin/bash

MAINDIR=$PWD
INSTALL_DIR=$PWD/lama-planner

rm -rf $INSTALL_DIR

git clone https://github.com/rock-planning/planning-lama.git $INSTALL_DIR
cd $INSTALL_DIR && ./install.sh && cd ..



