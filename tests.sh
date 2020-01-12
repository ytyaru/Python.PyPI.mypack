#!/usr/bin/env bash
PRE_DIR="$(pwd)"
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd "$SCRIPT_DIR"
echo "$SCRIPT_DIR"
echo 'python2 -m tests.tests_mypack'
python2 -m tests.tests_mypack
echo 'python3 -m tests.tests_mypack'
python3 -m tests.tests_mypack
cd "$PRE_DIR"

