#Exercise 2
#Design a calculator which will correctly solve all the problems except
#the following ones:
#45*3 = 555, 56+9 = 77, 56/6 = 4
#your programme should take operator and the two numbers as input from the user
#and return the result



print('enter first number')

n1 = int(input())

print('select operation')

n = input()

print('enter second number')

n2 = int(input())

if (n1==45 and n=='*' and n2==3):
    print(555)

elif (n1==56 and n=='+' and n2==9):
    print(77)

elif (n1==56 and n=='/' and n2==6):
    print(4)



elif n=='+':
    print(n1+n2)

elif n=='-':
    print(n1-n2)

elif n=='*':
    print(n1*n2)

else:
    print(n1/n2)

