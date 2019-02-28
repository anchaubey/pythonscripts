There are three ways to read data from a text file.

read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
File_object.read([n])

readline() : Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
File_object.readline([n])

readlines() : Reads all the lines and return them as each line a string element in a list.
  File_object.readlines()


with open("C:\\Users\\ankit\\Desktop\\test.txt","w+") as f:
    f.write("We are learning python\nWe are learning python\nWe are learning python")
    f.seek(0)
    print(f.read())
    print("Is readable:",f.readable())
    print("Is writeable:",f.writable())
    f.truncate(5)
    f.flush()
    f.seek(0)
    print(f.read())
f.close()

==========================================================

if f.mode == 'r':
==========================

Note: ‘\n’ is treated as a special character of two bytes

# Program to show various ways to read and
# write data in a file.
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
 
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
 
file1 = open("myfile.txt","r+") 
 
print("Output of Read function is ")
print(file1.read())
print()
 
# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0) 
 
print "Output of Readline function is "
print(file1.readline())
print
 
file1.seek(0)
 
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
 
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

===============================================

Apending to a file

# Python program to illustrate
# Append vs write mode
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file1.close()
# Append-adds at last
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","a")#append mode
file1.write("Today \n")
file1.close()
 
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()
 
# Write-Overwrites
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
 
file1 = open("C:\\Users\\ankit\\Desktop\\falcon.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()

