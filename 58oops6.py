#58
#static method
#we use static method to use it for class or instance and keep code precise
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

    @classmethod
    def from_str(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print('This is good'+string)
        return 'Thenga'    #if we write  only 'return' then none is printed in place of Thenga
harry = Employee('Harry', 255, 'Instructor')
rohan = Employee("Rohan",455, "Student")
karam = Employee.from_str('Karan-480-Student')

print(karam.printgood("Harry"))

#karam is instance
#Employee is class


