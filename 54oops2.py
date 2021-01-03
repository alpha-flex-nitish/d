#54
#diff bw instance and class variable
class Employee:    #class name start in capital: good practice
    no_of_leaves = 8
    pass

harry = Employee      #if we dont give () differernt format of .__dict__ of object is printed
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"


rohan.name  = "Rohan"

rohan.salary = 4554
rohan.role = "Student"
print(rohan.name, harry.salary, rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(rohan.__dict__)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)   #changed
rohan.no_of_leaves = 9         #only that of rohan changed
print(rohan.no_of_leaves)

print(rohan.__dict__)     #an attribute to return dict. and no. of leaves changed to 9 than 8 in {line28}
print(harry.__dict__)



















