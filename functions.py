a = 9
b = 8
c = sum((a,b))    # built in fun
#iterable(tuple and list) only iside of a sum function so 2 must brackets
print(c)

#user defined fun

def function1():
    print('Hello you are in function 1')

print(function1())
function1()
function1()
function1()
function1()  # fun1 executed every time we mention function1
             # used to exectute any code n number of times

def function1(a,b):
    print('Hello you are in function 1',a+b)

function1(5,7)

def function2(a,b):
    average = (a+b)/2
    print(average)

v = function2(5,7)
print(v)


def function2(a,b):
    average = (a+b)/2
    print(average)
    return average

v = function2(5,7)
print(v)


def function2(a,b):
    """This is a fun which will calculate average of two numbers
    this fun doesnt work for three numbers"""
    average = (a+b)/2
   # print(average)
    return average  #optional but necess to get a return or :none is output

#v = function2(5,7)
#print(v)
print(function2.__doc__)  # about descrp of fun




