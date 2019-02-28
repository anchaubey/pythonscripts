class Employee:
    def __init__(self, name, dept, salesMadeThisWeek):
        self.name = name
        self.dept = dept
        self.salesMadeThisWeek = salesMadeThisWeek

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved.")
        else:
            print("Tager is not achieved.")

    def sayHello(self):
        print("Say Hello", self.name)
        
employee1 = Employee('Ben','Sales',6)
employee2 = Employee('Sam','Marketing',4)
print(employee1.name)
print(employee2.name)
employee1.hasAchievedTarget()
employee2.hasAchievedTarget()
employee1.sayHello()
employee2.sayHello()
