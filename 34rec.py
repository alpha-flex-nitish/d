#34
def print2(str1):
    #return 'This is' + str1              # this goes into return value instead and not printing in output
    #print2()                             #:E becoz the process repeats itself star
    print('This is '+ str1)
print('harry')
print2('harry')



#Factorial using recursions (iterative and recursive)

# n! = n * n-1 * n-2 * n-3..........1
# n! = n * (n-1)!


#1: Factorial using iterative method
def factorial(n):
    """
    :param n:  Integer                              # kya leta hai
    :return:   n*n-1*n-2*n-3..........1             #kya deta hai
    """
    fac = 1
    for i in range(n):        #i humara 0 se chalu hoga aur n tak jayega range me (n) ki wajah se
        fac = fac *(i+1)
    return fac


number = int(input('Enter the number'))
print('Factorial using iteratve method',factorial(number))



#2: Factorial using recursive method
def factorial_recursive(n):
    """
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)          #space not necessary b/w * and f_r(n-1)
#In recurrsion stack, values gets stored
## 5 * factorial(4)
## 5 * 4 * factorial(3)
## 5 * 4 * 3 * factorial(2)
## 5 * 4 * 3 * 2 * factorial(1)
## 5 * 4 * 3 * 2 * 1 = 120

number = int(input('Enter the number'))               #number written in these two lines only
print('Factorial using recursive method',factorial_recursive(number))

#Recursion easier if we know mathematical formula
#Iterative requires more code writing but easy for debugging
#Quiz       X
"""
def fibonacci_series(number):
    #
    #     :param n: Integer
    #     :return: fibonacci_series(number-1) +fibonacci_series(number-2)
    #
    fib(1) = 0
    fib(2) = 1
    for i in range(number):
        #fib(i) = fib(i-1) + fib(i-2)
        fib(number) = fib(number-1) + fib(number-2)

    return fib
number = int(input('Enter the number'))
fibonacci_series()

print('fibonacci no. = ',fibonacci_series(number))


"""

def fibonacci_series(n):



    if n == 1:
        return 0
    if n ==2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

number = int(input('Enter the number'))
print('Fibonacci_series', number,'th term =',fibonacci_series(number))

#for removing space b/w 'number' and 'th term'
print('Fibonacci_series', number,end="")
print('th term =',fibonacci_series(number))   #*takes time for terms greater than 30
