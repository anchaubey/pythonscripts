class Employee:
    def __init__(self):
        self.name = 'Ankit'
        self.age = 24
    @staticmethod
    def helloyou():
        print("This is using static method")

obj1 = Employee()
obj1.helloyou()
