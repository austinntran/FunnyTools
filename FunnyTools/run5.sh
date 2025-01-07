#!/bin/bash
if [ "$#" -eq 0 ]; then
    command="$*"
else
    echo "command"
    read command  
fi
while [ 1 ]
do
  $command
  sleep 5s
done
