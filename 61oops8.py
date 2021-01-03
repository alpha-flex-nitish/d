#61
#multiple inheritence
#2 clases se ek class banana
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        var = 8
        self.name = aname
        self.salary = asalary
        self.role = arole
        # self.languages = alanguages

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}.'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print('This is good'+string)

class Player:
    no_of_games = 4
    var = 9
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f'Name is {self.name}. Game is {self.game}.'


class CoolProgrammer(Employee,Player):  #pahle karan = (jo bhi argument diya gaya hai) wo Sabse upar Employee claas me dhundega, then player class se apfne no. of variables aur aurgumnets match karega
    var = 10
    language = "C++"
    def printlanguage(self):   # a method
        print(self.language)   #this is must to print"C++" by usingdet = karan.printdetails()\n karan.printlanguage()
     # pass                     #must be removed once its not empty


#2 instances below and a class above
harry = Employee('Harry', 255, 'Instructor')
rohan = Employee("Rohan",455, "Student")

shubham = Player("Shubham", ["Cricket"])

karan = CoolProgrammer("Karan",8999,"coolProgrammer")

det = karan.printdetails()
karan.printlanguage()

print(det)

print(karan.var)
#if we eliminate coolProgrammer var, we have to change karan = no. of values
#equal to that of employee class and then it will print employee var value
#bz of "class CoolProgrammer(Employee,Player):" this sequence















