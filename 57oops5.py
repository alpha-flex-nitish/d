#57
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):   #jo normal method hota hai jo hum class me istemal karte hai wo self as an argument le leta hai
        self.name = aname                     #eg. self le lia >__init__ constructor ne, printdetails ne
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):   #jab hame self nahi chahiye hota sirf class chahiye hota hai tab hum class banate hai
        cls.no_of_leaves = newleaves    #jab hame na instance variable chahiye na class variable chahiye tab file 58 dekho

    # @classmethod
    # def from_str(cls, string):
    #     params = string.split('-')              #params becomes a list
    #     print(params)
    #     return cls(params[0],params[1],params[2])   #constructor
    #                                                 #here print(params) donot work

    #one liner for above para(:-)>--(**)-+=((***))]zzzsC=====D
    @classmethod
    def from_str(cls, string):
        return cls(*string.split('-'))

harry = Employee('Harry', 255, 'Instructor')
rohan = Employee("Rohan",455, "Student")
karam = Employee.from_str('Karan-480-Student')

print(karam.no_of_leaves)
print(karam.salary)

# here print(params) donot work


print(harry.no_of_leaves)
Employee.no_of_leaves = 89
print(harry.no_of_leaves)

harry.change_leaves(34)
print(harry.no_of_leaves)

print(Employee.no_of_leaves)






