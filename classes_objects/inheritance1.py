class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
            return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)
            print("Salary after raise is: ", self.pay)
            
class Developer(Employee):
    pass

dev_1 = Employee('Ankit', 'Chaubey', 30000)
dev_2 = Employee('Amit', 'singh', 40000)

devel = Developer('Sachin', 'Dehar', 25000)

#print(dev_1.first)
#print(dev_1.last)
#dev_1.fullname()
print(devel.first)
devel.apply_raise()
