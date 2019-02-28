#Tuples - immutable lists (their contents cannot be changed by adding, removing or replacing elements)
my_tuple = () #creating an empty tuple
 
my_tuple = (9,) #creating a tuple with a single element; DO NOT forget the comma
 
my_tuple = (1, 2, 3, 4)
 
#Tuples - the same indexing & slicing rules apply as for strings and lists
len(my_tuple) #returns the number of elements in the tuple
 
my_tuple[0] #returns the first element in the tuple (index 0)
my_tuple[-1] #returns the last element in the tuple (index -1)
my_tuple[0:2] #returns (1, 2)
my_tuple[:2] #returns (1, 2)
my_tuple[1:] #returns (2, 3, 4)
my_tuple[:] #returns (1, 2, 3, 4)
my_tuple[:-2] #returns (1, 2)
my_tuple[-2:] #returns (3, 4)
my_tuple[::-1] #returns (4, 3, 2, 1)
my_tuple[::2] #returns (1, 3)
 
#Tuples - tuple assignment / packing and unpacking
tuple1 = ("Cisco", "2600", "12.4")
 
(vendor, model, ios) = tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements
 
(a, b, c) = (1, 2, 3) #assigning values in a tuple to variables in another tuple
 
min(tuple1) #returns "12.4"
 
max(tuple1) #returns "Cisco"
 
tuple1 + (5, 6, 7) #tuple concatenation
 
tuple1 * 20 #tuple multiplication
 
"2600" in tuple1 #returns True
 
784 not in tuple1 #returns True
 
del tuple1 #deleting a tuple
