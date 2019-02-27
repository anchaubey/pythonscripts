#!/usr/bin/python3.5

import telnetlib
import getpass

def telnet_connection():

#prompt to enter the remote computer name
remote_computer = input(“Enter computer name: “)
#prompt to enter the remote computer username with access to make changes
username = input(“Enter computer username :”)
#prompts for the above users password
password = getpass.getpass()

print(“hostname is : %s” %remote_computer)
print(“The username is : %s” %username)
print(“password is: %s” %password)

#Creates an instance of Telnet for connection to remote machine
#a timeout value is given so that errors are displayed wihtin the time
#and errors do not take indefinite time
connection = telnetlib.Telnet(remote_computer, timeout=10)

print(“Trying to connect to remote system…”)
#telnet interface works with bytes and Unicode
#use .encode to convert to bytes and ascii to make it unicode
connection.read_until(“login: “.encode())
connection.write((username + “\n”).encode(‘ascii’))
print(“Successfully written username”)

connection.read_until(“Password: “.encode())
connection.write((password + “\n”).encode(‘ascii’))
print(“successfully written password”)

#write the command to be executed to remote system telnet console

connection.write((“sudo apt-get install telnetd\n”).encode(‘ascii’))

print(“Displaying the content of the installation in a second.”)

connection.write((“exit\n”).encode(‘ascii’))

print(“Exiting ….”)
#Displays the output of the command on your python console
output = connection.read_all()

print(output)

if __name__ == ‘__main__’:
telnet_connection()
