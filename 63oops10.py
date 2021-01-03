# Public _ normal variables and normal name given
# Protected - use _ before names  (base class and classes derived from it can use it
# Private - use__ before names    And._Employee before privatevariablename to acces it

class Employee:
    no_of_leaves = 8
    _protec = 9
    __private = 98
    def __init__(self,aname,asalary,arole):
        var = 8
        self.name = aname
        self.salary = asalary
        self.role = arole

emp = Employee("harry",343,"Programmer")
print(emp._protec)
# print(emp.__private):E
print(emp._Employee__private)




