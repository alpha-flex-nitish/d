print('Enter num1')
num1 = int(input())   # Error in line2 if we enter a alphabet and number rept.
print('Enter num2')
num2 = int(input())
print(num1+num2)
print('The Sum of these two number is',num1+num2)

print('Enter num1')
num1 = input()
print('Enter num2')
num2 = input()
print(num1+num2)
#print('The Sum of these two number is',int(num1)+int(num2) # Error in line6 if we enter a alphabet and number rept.


try:
    print('The sum of these two numbers is',
          int(num1)+int(num2))
except Exception as e:      #prints error as it is whatever error in taking input or in your code like if we write int as imt it gets printed
    print(e)       #mostly we use this code while delaing with internet connections

print('This line is very important')   #our most imp line that must be executed even if sum code(line6) fails


