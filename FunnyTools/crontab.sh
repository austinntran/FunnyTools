#!/bin/bash

echo "command"
read command
crontab -l | { cat; echo "*/1 * * * * $command"; } | crontab -

# currentcron="$(crontab -l 2>/dev/null)"
# newcron="$currentcron
# * * * * * $command"
# echo "$newcron" | crontab
