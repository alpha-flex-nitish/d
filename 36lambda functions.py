#Lambda functions or anonymous functions
def add(a,b):
    return a+b

#we want a fun for this work but we dont want use function


minus = lambda x, y: x-y
print(minus(9,5))
#is same as

def minus(x,y):
    return x-y
print(minus(9,5))

def a_first(a):         #Takes input as 'a' and
    return a[1]         #And returns a[1] and prints it if we write print

a = [[1,44],[5,36],[8,23]]
a.sort(key=a_first)      #key is an argument in sort that takes a fun as input and with the help of this fun we sort list
                         #and returns a[1] or first index or second elements inside of every sub-list
print(a)                 # now we will make a function named a_first 2 lines above list a

a = [[1,84],[5,36],[8,53]]
a.sort(key=a_first)
print(a)

a = [[1,84],[5,6],[8,53]]
a.sort(key=lambda x:x[1])  #x:x[1];ek aisa fun x bana do jo ki return kare x[1]
                           #koi bhi list usko di jaye to uska 2nd element; 0 for 1st element
print(a)                   #sort fun ki prop. hoti hai ki key= fun ka naam leta hai

a = ['233','2dddd','4d']   #' ' are must here
a.sort(key=len)
print(a)
