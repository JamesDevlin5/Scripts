#!/usr/bin/env bash

# Plugin Download Directory
TARGET_DIR="$HOME/.config/mypy/"

# Declare Array
declare -a PLUGINS

# Plugin Targets
PLUGINS=(
    "https://raw.githubusercontent.com/python/mypy/master/mypy/plugins/functools.py"
    "https://raw.githubusercontent.com/python/mypy/master/mypy/plugins/enums.py"
    "https://raw.githubusercontent.com/python/mypy/master/mypy/plugins/dataclasses.py"
)

# Make Target Directory If Necessary
if [ -n "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
fi

# Download
for TARGET in "${PLUGINS[@]}"; do
    BASE="$(basename "$TARGET")"
    curl -sL -o "$BASE" "$TARGET_DIR""$TARGET"
    printf "Downloaded:\t%s\n" "$BASE"
done
