class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 85, "Cleaner")
# print(emp1+emp2):E
#     def __add__(self, other):
#         return self.salary + other.salary
# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 85, "Cleaner")
# print(emp1+emp2)
#once we commonted above para then only we get neo for following para (irs true onley when we give a tab space in def not if we startt with 0 space  (star)
#st its workin st not
#     def __truediv__(self, other):
#         return self.salary / other.salary
# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 85, "Cleaner")
# print(emp1 / emp2)

# mapping operators to functions
# dundder method

# print(emp1)


    def __repr__(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'
emp1 = Employee("Harry", 345, "Programmer")      #def ke baad hi class likho pahle nahi

print(emp1)

# def __repr__(self):
#     return f"Employee({self.name}, {self.salary}, {self.role} "
#
# emp1 = Employee("Harry", 345, "Programmer")
# print(emp1)

#one at a time is working perfectely having def with indentation
# otherwise <__main__.Employee object at 0x01753670> is  printed
#in place of Name is Harry. Salary is 345 and role is Programmer

    def __str__(self):
        






