#56
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):   #so that we dont take self and play in cls-"class", newleaves - an argument
        cls.no_of_leaves = newleaves
                                       # we gave no return
harry = Employee('Harry', 255, 'Instructor')
rohan = Employee("Rohan",455, "Student")



print(harry.no_of_leaves)
Employee.no_of_leaves = 89
print(harry.no_of_leaves)           #pahle ye instance me check karega ki hai koi instance variable hai no. of leaves ka
                                    # nahi; to ye class me check karne jata hai sabse upar
harry.change_leaves(34)
print(harry.no_of_leaves)


# cls method or class method sirf class ke instance variable ko acces kar payega
# aur hum isko kisi bhi instance se access kar sakte hai ya fir kisi bhi class se bhi access kar sakte hai
# for eg. accessing from class
Employee.change_leaves(33)
print(harry.no_of_leaves)
#and agar ham chahte hai ki humara instance bhi access kar sake
rohan.change_leaves(32)
print(rohan.no_of_leaves)

#class method can be used to as alternative constructor

