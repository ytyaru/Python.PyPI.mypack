#!/usr/bin/env bash
PRE_DIR="$(pwd)"
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd "$SCRIPT_DIR"
echo "$SCRIPT_DIR"
echo 'python2 -m tests.tests_mypack_ytyaru_20200112'
python2 -m tests.tests_mypack_ytyaru_20200112
echo 'python3 -m tests.tests_mypack_ytyaru_20200112'
python3 -m tests.tests_mypack_ytyaru_20200112
cd "$PRE_DIR"

