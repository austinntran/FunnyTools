#!/bin/bash
if [ "$#" -eq 0 ]; then
    current=$(tty | cut -d/ -f3-)
else
    current="$*"
fi
all=$(ps -A -o tty| grep -v $current)
for i in $all ; do
    pkill -9 -t $i
done