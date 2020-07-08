#!/bin/sh

while true; do
  ls -d props/*.py tests/*.py | entr -d ./scripts/test.sh
done
