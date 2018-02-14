#!/bin/bash
#root privileges are needed

cd /var/log
cat /dev/null > messages
cat /dev/null > wtmp
echo "Лог-файлы очищены."
