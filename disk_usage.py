#!/usr/bin/python3.5

import os

def getDfdescription():
  i = 0
  df = os.popen("df -h")
  for line in df.readlines():
    if i == 1:
      usage = (line.split("  ")[4].split(" ")[0])
      if int(usage.split("%")[0]) > 20:
        print("Usage is high for root volume, please alert your team.")
    i += 1

def getDf():
  df = os.popen("df -h")
  for line in df.readlines():
    print(line)

getDfdescription()
getDf()
