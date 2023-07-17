#!/bin/sh

eips -c 

eips 0 0 "starting program"

iptables -A INPUT -p tcp --dport 5000 -i wlan0 -j ACCEPT
echo "opened"
mntroot rw
echo "writeable"

eips 0 0 "port opened and made writeable"

cd /mnt/us/kindlefusion; /usr/bin/python3 /mnt/us/kindlefusion/stable17.py  2&>1 | tee logfile.log

