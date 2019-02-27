'''Sometimes we want to initiate our subclasses, with more information
than our parent class can handle. Suppose we also want to add a programming
language for these developers as an attribute.
Now our employee class only accepts first name, last name and pay.
So, if we also wanted to add the programming language.
In Python 3 and above, the syntax for super is:
super function can be used to gain access to inherited methods –
from a parent or sibling class – that has been overwritten in a class object.

super().methoName(args)

'''

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
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Employee('Ankit', 'Chaubey', 30000)
dev_2 = Employee('Amit', 'singh', 40000)

devel1 = Developer('Sachin', 'Dehar', 25000, 'Python')
devel2 = Developer('Sachin', 'Dehar', 25000, 'Java')

#print(dev_1.first)
#print(dev_1.last)
#dev_1.fullname()
print(devel1.prog_lang)
print(devel2.prog_lang)
