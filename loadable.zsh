#!/usr/bin/env zsh

# View all functions that may be autoloaded by the environment
# (All functions on fpath)


for item in $fpath; do
    echo '------'
    echo $item
    echo '----'
    ls $item | nl -w 4
    echo
done |
    nl -ht -bn -p -d '--' -n ln -w 4 |
    $PAGER


