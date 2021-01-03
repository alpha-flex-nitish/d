#39
#F strings
#string formatting:Inserting variable in b/w a string
#When we write a string:-statement and want to insert
#a variable in that line or statement we use string formatting

#1 way to do string formatting: hard to use if variable no. increases
me = 'Harry'
a =  'this is %s'%me  #This is a string not a F-string but it is string formatting only
print(a)              #agar hum string formatting karte hai to ye 'me' variable ka naam;'Harry' ko
                      #%s ke jagah pe daal dega


#2 way of string formatting using tuple: its un-readable
me = 'Harry'
a1 =3
#a = 'this is %s'%(me,a1) #:E ;cause only 1 %s written # % ke baad ek tuple diya hua hai:-(me,a1)
a = 'this is %s %s'%(me,a1)
print(a)

#3 way of string formatting using .format: readability meshup

me = 'Harry'
a1 =3
a = 'This is {} {}'

a.format(me,a1)    #Use-
print(a)           #less

b = a.format(me,a1)
print(b)

c = 'This is {1} {0}'    #variable sequencially put accn to numbering
print(c)
d = c.format(me,a1)
print(d)



#4 F-strings :overcome above 3 methods of string formatting
#Jab strings ko silna ho to fstrings ka istemaal karna chaiye
me = 'Harry'
a1 = 3
a = f'This is {me} {a1} {4*65}'  #we can use functions, module ke andar functions,
                                 # python variable expressions too here;4*65
print(a)                         #f means its a F-sting f:Fast

import math                      #imported module: math
a = f'This is {me} {a1} {4*65} {math.cos(65)}'
print(a)

#object oriented programming__str, __repr !r
#import time
#time module to find time of programme execution time



