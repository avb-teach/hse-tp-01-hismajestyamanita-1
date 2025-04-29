#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./collect_files.sh input_dir output_dir [--max_depth N]"
    exit 1
fi

python3 collect_files.py "$@"
