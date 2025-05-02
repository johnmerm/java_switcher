#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
#execute python set_java.py with arg1
out=$(python "$SCRIPT_DIR/set_java.py" "java23")

IFS=$'\n'
for line in $out;do
#  echo "$line"
  eval "$line"
done