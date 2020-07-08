#!/bin/sh

while true; do
  ls -d scrubbish/*.py tests/*.py | entr -d ./scripts/test.sh
done
