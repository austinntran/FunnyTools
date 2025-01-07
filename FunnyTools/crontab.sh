#!/bin/bash

echo "command"
read command
crontab -l | { cat; echo "*/1 * * * * /bin/bash -c '$command'"; } | crontab -
