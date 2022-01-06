#!/bin/bash

set -ex

mkdir repos
REPOS=$PWD/repos

git clone https://github.com/flatironinstitute/FMM3D $REPOS/FMM3D
cd $REPOS/FMM3D
make install
make python

git clone https://github.com/fastalgorithms/fmm3dbie.git $REPOS/fmm3dbie
cd $REPOS/fmm3dbie
make install
make python

git clone https://github.com/mrachh/miniwasp $REPOS/miniwasp
cd $REPOS/miniwasp
make python