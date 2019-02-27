#!/usr/bin/python3.5

list = ['ankit', 'ankit1', 'ankit2', 'ankit3']
setuid = set()

file = open('/etc/passwd').read()
for line in file.split("\n"):
  split = line.split(":")
  setuid.add(split[0])

list1 = []
for i in list:
  if i in setuid:
    list1.append(i)

print("The users found are: ")
print(list1)
