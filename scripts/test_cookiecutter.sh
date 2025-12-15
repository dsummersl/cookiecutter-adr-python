#!/usr/bin/env bash

# nounset: undefined variable outputs error message, and forces an exit
set -u
# errexit: abort script at first error
set -e
# print command to stdout before executing it:
# set -x

rm -rf ./project-alpha || true
uvx cookiecutter --no-input .

cd project-alpha

make setup
make ci
