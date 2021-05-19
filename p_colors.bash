#!/usr/bin/env bash

for i in {0..255}; do
    tput setab "$i"
    printf "%4s" "$i"
done

tput sgr0

