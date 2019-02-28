#!/usr/bin/python3.5

#Functions - Basics
def my_first_function(x, y): #defining a function that takes two parameters
    sum = x + y
    return sum #this statement is used to exit a function and return something when the function is called
    
my_first_function(1, 2) #calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3
 
my_first_function(x = 1, y = 2) #calling a function and passing two KEYWORD arguments, the values of 1 and 2; result is 3
 
my_first_function(1, y = 2) #calling a function and passing mixed types of arguments, the values of 1 and 2; result is 3; rule: positional arguments always before keyword arguments!
 
def my_first_function(x, y, z = 3): #specifying a default parameter value in a function definition
 
def my_first_function(x, *args) #specifying a variable number of positional parameters in a function definition; args is a tuple
 
def my_first_function(x, **kwargs) #specifying a variable number of keyword parameters in a function definition; args is a tuple
 
global my_var #"importing" a variable in the global namespace to the local namespace of a function


#!/usr/bin/python3.5

def func1():
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))
  print(x+y)


func1()
