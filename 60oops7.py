#60
#single inheritence
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

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

class Programmer(Employee):
    def __init(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages
    def printprog(self):
        return f'The Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role} and the languages are {self.languages}.'

harry = Employee('Harry', 255, 'Instructor',"eng")
rohan = Employee("Rohan",455, "Student","hin")

shubham = Programmer("Shubham", 555, "Programmer",["python","vpp"])
karan = Programmer('Karan',777,"Programmer","cpp")
print(karan.printprog())
print(karan.printdetails())
print(karan.printprog())
#languages in line5 and line9are perhaps compulsory in this version of python
#to make it similar to line27 and line31



