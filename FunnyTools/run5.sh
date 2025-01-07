#!/bin/bash
if [ "$#" -eq 0 ]; then
    echo "command"
    read command  
else
    command="$*"
fi
while [ 1 ]
do
  $command
  sleep 5s
done
