##Operators
#Arithmetic operators
#Assignment operators
#Comparision operators
#Logical operators
#Identity Operators
#Membership ooperators
#Bitwise operators

#Arithmetic operators
print('5+6 is',5+6)
print('5-6 is',5-6)
print('5*6 is',5*6)
print('5/6 is',5/6)
print('5**3 is',5**3)
print('5%6 is',5%6)
print('5//6 is',5//6)



#Assignment operators
print('Assignment operators')
x = 5
print(x)
x +=7
print(x)

x -=7
print(x)

x *=7
print(x)

x /=7
print(x)

x %=7   # x = x%7
print(x)




#Comparision operators
i =5
print(i == 9)
print(i == 5)
print(i >= 5)
print(i != 5)
# star
print(i and 5)
print(i or 5)
print(i or 4)
print(i and 4)



#Logical operators
a = True
b = False

print(a and a)  # both must be true for it to be true
print(a and b)

print(a or a)  # if any one ofthem true it is true
print(a or b)





#Identity operators
print(a is b)
print(a is not b)
print(5 is not 7)
print(5 is not 5)





#Membership ooperators
list = [3,3,2,2,39,33,35,32]

print(32 in list)
print(324 in list)
print(324 not in list)




#Bitwise operators~ 3 ya 1 ke sath kam karta hai
#0 - 00
#1 - 01
#2 - 10
#3 - 11

print(0 & 1)  # :0
# 0 0
# 0 1
#------   {0 and 0 = 0} in first VR line,  {0 and 1 = 0} in sec VR lin~~00
#+0 0  :~0 (output)
print(0 | 1)
#  0 0
#  0 1
#------   {0 or 0 = 0} in first VR line,  {0 or 1 = 1} in sec VR lin~~01
#or0 1  :~1(output)

print(0 | 3)
#  0 0
#  1 1
#------   {0 or 1 = 1} in first VR line,  {0 or 1 = 1} in sec VR lin~~11
#or1 1  :~3(output)

print(0 & 2)

#not xor zero fill left shift right shift:boolean


