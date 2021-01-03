#38
#Using Module

import random     # Random is a module to select random no.

random_number = random.randint(0,5)   #including 0 and 5 both we will get a random integer from 0 to 5 by(0,5)
print(random_number)                  #till we write random in prev. line color of module name is grey both
                                      #in line 4 and line 6. Un-used initiated module in our
                                      #programme color remains grey  its an indication that your
                                      #random module intialized in line is unused. used color = blue
rand = random.random()       #random module ke andar random fun
print(rand)                  #ye generate karta hai 0se 1 tak random real no. upto 1+14/1+16/ 1+17 decimal places
                             #kabhi kabhi module ke andar ek sub-module hota hai


#rand1 = random.random.random()    #:E
#print(rand)

rand = random.random()*100          #ye generate karta hai 0se 100 tak random real no. upto 2+13/ 2+14/ 2+15/ 16 decimal places
print(rand)

rand = random.random()*10000         #ye generate karta hai 0se 10000 tak random real no. upto 4+11/4+12/ 3+13/ 4+13/ 3+14/ decimal places
print(rand)
                                    #conclusion: generates random no.

#Random.choice

list = ['Star Plus','DD1','Aaj Tak','Code With Harry']
#choice = choice.random(list)#:E
random.choice(list)

choice = random.choice(list)    #or choice = random.choice('Star Plus','DD1','Aaj Tak','Code With Harry')
print(choice)
#Some module are inbuilt, we can install module by
##Terminal->pip install sklearn

#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________




#Random module

a = random.choice('computer')
print('a',a)
#This:
list = ['Star Plus','DD1','Aaj Tak','Code With Harry']
choice = random.choice(list)
print(choice)
#Can also be written as;s
b = random.choice(['Star Plus','DD1','Aaj Tak','Code With Harry'])    #[] are must
print('b',b)

c = random.choice([12,23,45,67,65,43])
print('c',c)

d =  random.shuffle([12,23,45,67,65,43])#  d = random.shuffle(numbers)   OR d = random.shuffle('numbers')  :E
print('d',d) #NNNNNOOOOO
print('d',([12,23,45,67,65,43]))


numbers = [12,23,45,67,65,43]
e = random.shuffle(numbers)
print('e',numbers)       #if print(e)   :NEO:None

mylist = ["apple", "banana", "cherry"]
f = random.shuffle(mylist)
print('f',mylist)        # if print(f)   :NEO:None


#random.randrange():          #Returns a randomly selected element from the range created by the start,
                              # stop and step arguments. The value of start is 0 by default.
                              # Similarly, the value of step is 1 by default.
g = random.randrange(0,101,10)
print('g',g)

# h
citylist = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("h Pick 2 Random element from list:", random.sample(citylist, 2))



import random
import secrets

number = random.SystemRandom().random()
print("i secure number is ", number)                #0.15828449764841612
                                                  #0.9391253615126653
                                                  #0.1060388629272383

print("j Secure byte token", secrets.token_bytes(16))  #b'e\x0f\x82\x04\xa6\xf1F\xec~\xb2\xefC\x1bac\x8b'
                                                     #b'\xb6\x8d>\xf8sHJu\xb7\xe8\xc6\xccyc\x9a\x88'
                                                     #b'\x0c\xf2\xcd\x11;\x93\xeb\x9dD\xa3\x0e\x19\x83\xc8\x174'

 #random.triangular star, random.seed(a=None, version=2),  random.shuffle(x[, random])  ;-why x here




print('k',"floating point within given range",random.uniform(10.5, 25.5)) #not same as #print('l',random.random(10.5, 25.5))  :E
                                                                          # OR  print('l',random.random(5,10)) :E

print('l',random.random())    #only true for no value specified and returns only number b/w  and 1


d1 =  random.shuffle([12,23,45,67,65,43])
print(d1)  #:None
print(random.shuffle([12,23,45,67,65,43]))
#OR

l = [12,23,45,67,65,43]
print()