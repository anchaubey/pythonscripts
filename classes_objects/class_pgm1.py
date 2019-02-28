#Instance attributes in python and the init method
#You can also provide the values for the attributes at runtime.
#This is done by defining the attributes inside the init method.
#The following example illustrates this.

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self):
        print("The name of snake is", self.name)


python = Snake("python")
anaconda = Snake("anaconda")
python.change_name()
anaconda.change_name()
