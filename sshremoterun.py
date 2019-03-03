#!/usr/bin/python

import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='52.53.152.193', username='ankit', password='redhat')

choice = input("Please enter 1 for cpu usage and 2 for disk usage: ")

if choice == '1':
    command = 'top -n 1 -b'
elif choice == '2':
    command = 'df -h'
else:
    print("Please provide a valid input.")
    sys.exit()

stdin, stdout, stderr = ssh.exec_command(command)

for line in stdout.read().splitlines():
    print(line.decode('utf8'))

ssh.close()


