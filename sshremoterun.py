#!/usr/bin/python

#!/bin/python
import sys
import os

data = {"user": "ankit",
        "host": "172.31.4.101",
        "password": "redhat",
        "commands": " " .join(sys.argv[1:])}

command = "sshpass -p {password} ssh {user}@{host} {commands}"
os.system(command.format(**data))
