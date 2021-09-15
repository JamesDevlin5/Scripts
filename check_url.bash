#!/usr/bin/env bash

if [[ $# -eq 0 ]]; then
    echo "No URL provided! Exiting..."
    exit 1
fi

URL="$1"

status="$(curl --head --fail --silent "$URL" | head -n 1 | cut -f 2 -d' ')"
prefix="${status::1}"

case "$prefix" in
    "1") printf "[%s] %s\n" "$status" "Informational";;
    "2") printf "[%s] %s\n" "$status" "Successful";;
    "3") printf "[%s] %s\n" "$status" "Redirect";;
    "4") printf "[%s] %s\n" "$status" "Client Error";;
    "5") printf "[%s] %s\n" "$status" "Server Error";;
    *) printf "[%s] %s\n" "$status" "Unkown Response Code";;
esac

