#51

def function1():
    print('Subscribe now')

func2 = function1    #func2=function1() likh dete to function call ho jata
                     #instead here we assigned func2=function1
del function1        #still subs now is printed kyuki function2 ki ek dusri copy ban chuki hai
                     #even if we delete fun1
func2()

# function returner:-
#ek function ke dwara ek function ko return kar sakte hai
def funcret(num):
    if num==0:
        return issubclass
    if num==1:
        return sum
    if num==2:
        return print
    if num==3:
        return print()
b = funcret(5-4)
print(b)
a = funcret(78*0)
print(a)
c= funcret(2)
print(c)
d = funcret(3)
print(d)            #prints a plane line and None in new line
print('end1')
#function ko as an argument
def executor(func):
    func()          #prints a plane line and None in new line
    func('this')
    func('that')
executor(print)     #executoe chala ke print, #executor(print()) :E
#executor()         #:E
#executor(sum)      #function ke andar ham function daal sakte hai as an argument
                    #aur hum functions dwara functions ko return bhi kar sakte hai
                    #:E#but obvious sum yaha kaam nahi karega kyuki sum integer ko leta hai

#DECORATORS
def dec1(func1):    #dec1 naam se ek fun and uske andaar func1 naam se ek argument
    def nowexec():
        print('Executing now',2*3)
        func1()
        print("Executed")
    return nowexec() #is fun ko return kar diya

def who_is_harry():
    print('Harry is a good boy')

# who_is_harry()
who_is_harry = dec1(who_is_harry)    #() must not be present at both places after who_is_harry
                                     #perhaps it closes the fun and we must comment above eho_is_harry() above to execute just above line
                                     #as it gets called even after being closed
who_is_harry     #this line is must to execute just above line
                 #idk why who_is_harry() in above line is E
print('end',2,'\n')


#isa____________Is Same As
@dec1            #form of a decorator
def who_is_harry():
    print('Harry is a very good boy')
who_is_harry

#jab hamko ek hi kaam 10 func ke saath karna hai to hum uska dec bana lenge
#yani ek blueprint bana lenge aur dec1 dec1 karke use karta phirunga








