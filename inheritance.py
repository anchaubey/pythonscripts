#!/usr/bin/python3.5

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
    
    def __init__(self, first, last, pay, prog_lang, nationality):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.nationality = nationality

class Sales(Employee):

    def __init__(self, first, last, pay, salesMadeThisWeek,targetAchieved):
        super().__init__(first, last, pay)
        self.salesMadeThisWeek = salesMadeThisWeek
        self.targetAchieved = targetAchieved
    def hasAchievedtarget(self):
        if self.salesMadeThisWeek >= 5:
            print("{} has achieved the target.".format(self.first))
        else:
            print("{} has not achieved the target.".format(self.first))

        
dev_1 = Developer('Ankit', 'Chaubey', 30000, 'Python', 'India')
dev_2 = Developer('Amit', 'singh', 40000, 'Java', 'American')

dev_1.apply_raise()
print(dev_1.fullname())

'''
print(dev_1.pay)
print(dev_1.prog_lang)
print(dev_1.nationality)

salesman1 = Sales('Ankit', 'Chaubey', 10000,10, 'Yes' )
print(salesman1.targetAchieved)
salesman1.hasAchievedtarget()
print(salesman1.raise_amt)
'''
