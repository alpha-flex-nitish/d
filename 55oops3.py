#55
#about method?
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):   #.__init__ :-constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):                   #jab ham rohan.printdetails likhenge to self rohan ho jayega bas
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

harry = Employee('Harry', 255, 'Instructor')
rohan = Employee('Rohan',455,"Student")

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"


rohan.name  = "Rohan"
rohan.salary = 455
rohan.role = 'Student'
print(rohan.printdetails())
print(harry.printdetails())


print(rohan.no_of_leaves)
print(harry.salary)



