#!/bin/bash
current=$(tty | cut -d/ -f3-)
all=$(ps -A -o tty| grep -v $current)
for i in $all ; do
    pkill -9 -t $i
done