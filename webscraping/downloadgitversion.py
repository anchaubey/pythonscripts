#!/usr/bin/python3.5

#apt-get install python3-bs4
#apt-get install python-pip
#pip install requests


=====================

#!/usr/bin/python3.5

import os, subprocess

os.system('apt-get update -y')
os.system('apt-get install python3-bs4 -y')
os.system('apt-get install python-pip -y')
os.system('pip install requests')
os.system('pip install BeautifulSoup')
os.system('./script2.py')


==================================
import requests
from bs4 import BeautifulSoup
import re, sys, os
from subprocess import *

print("Welcome to automation part1.")
print("Installing the basic packages first...........")
print('Installing wget, unzip, vsftpd, telnet,apache2')
os.system('apt-get update -y')
os.system('apt-get install wget unzip vsftpd telnet apache2 -y')

print("basic packages installed.")

url = "https://mirrors.edge.kernel.org/pub/software/scm/git/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")
list1 = []
pattern = r'git-\d+\.\d+\.\d\.tar.gz'
for link in links:
        string = link.get("href")
        if re.match(pattern,string):
            list1.append(string)
        else:
            pass

pattern1 = '\d+\.\d+\.\d'

print("Now installing git..")

for item in list1:
    print((re.findall(pattern1,item)[0]),end='\t')

version = input("\nPlease provide your selection from the following: ")
link = "https://mirrors.edge.kernel.org/pub/software/scm/git/git-" + version + ".tar.gz"

dir = '/root/testing/'
download_tar_gz = "wget " + link + " -P" +  dir
install_cmd = "tar -xvf " +  dir + "git-" + version + ".tar.gz"
os.system(download_tar_gz)
os.system(install_cmd)


=========================================================================


def ansible():
    url = "https://releases.ansible.com/ansible/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a")
    pattern2 = 'ansible-\d+\.\d+\.\d\.tar.gz'
    list1 = []
    for link in links:
        string = link.get("href")
        if re.match(pattern2,string):
            list1.append(string)
        else:
            pass

    pattern3 = '\d+\.\d+\.\d'

    for item in list1:
        print((re.findall(pattern3,item)[0]),end='\t')

ansible()
