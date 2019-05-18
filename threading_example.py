import time
import threading

def calc_square(numbers):
    print("Calculate square numbers \n")
    for n in numbers:
        time.sleep(0.2)
        print('square : ',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        time.sleep(0.2)
        print('cube : ', n*n*n)


arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)

print("done in : ",time.time() -t)
print("hah... I am done with all my work now!")

