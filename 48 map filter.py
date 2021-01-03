#48
#map, filter, reduce
print('MAP')
numbers = ['3', '34', '64']
# for item in numbers:      #converting string to integer
#     item = int(item)      #did not work

# for i in range(numbers):



#range ke andar jo bhi cheej honi chaiye wo number honi chaiye
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1

#check
print(numbers[2])   #64 + 1 =65
#____________________MAP__________________________________
# for all above we can do in one line
# using map

#map({wo function jo is-->> list ke sare element pe apply ho jaye}, {wo list jis pe aap apply karna chahte hai} )
# map(int,numbers)  #E bz map object return karta hai so we need to convert it into list
numbers = ['3', '34', '64']
numbers = list(map(int,numbers))  #to convert that object into list

print(map(int,numbers))  #returns map object

# now string is converted into integer

def sq(a):
    return a*a
num = [2,3,5,6,76,7,3,3,2]
square = list(map(sq, num))
print(square)
#aliter
#map with lambda
num = [2,3,5,6,76,7,3,3,2]
square = list(map(lambda u:u*u, num))
print(square)




def square(p):
    return p*p

def bisquare(j):
    return j*j*j*j
import math
def cube(p):
    return p*p*p
x = [8,5,4,54]
function1 = [square, cube, bisquare, lambda v:v*2,  math.sqrt]  #(square)*(cube) E, # cannot write import.math inside function list in this line
for k in range (4):
    val = list(map(lambda y:y(k), function1))    #jab bhi map likhenge to map aur list dono sath likhenge
    print(val)                                   #function1 is nothing but a list
    pal = list(map(cube, x))                     #y:y(k)ek aisa function y jisme k dala jata hai to list-function1 ke sare element pe apply hota hai:- square, cube...
    #print(x)
    #print(pal)

#_____________________FILTER________________________

print('\nFILTER')


list_1 = [1,23,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5                                 #returns true or false
gr_than_5 = filter(is_greater_5, list_1)         #we have to typecast it into list otherwie object is printed
print(gr_than_5)
gr_than_5 = list(filter(is_greater_5, list_1))    #filter(function, iterable)
print(gr_than_5)
#____________________REDUCE__________________
print('\nREDUCE')

from functools import reduce

list1 = [1,2,3,4,2]                        #we want sum of all num in list
num = 0
for i in list1:
    num = num + i
print(num)
#aliter #using reduce
num = reduce(lambda x,y:x+y, list1)                 #reduce(function, sequence)#reduce(kya mai lagana chahta hu,
print(num)
num = reduce(lambda x,y:x*y, list1)
print(num)
