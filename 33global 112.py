#33
# def function1(n):
    print(n,'I have printed')

function1('This is me')


print('1\n')
l = 10                   #global varible; any no. of functons can use this variable in this programme
def function1(n):
    #l = 5                #local variable
    m = 8
    #l = l + 5            #E:without 'global' keyword, value of global cant be changed inside of local
    print(l,m)
    print(n,'I have printed')

function1('This is me')    #this line is must to print line{13} and {14} elements
#print(m)                 #:E searches only in global and not inside of any function urf local

print('2\n')

l = 10
def function1(n):
    m = 8
    global l
    l = l + 45
    print(l, m)
    print(n, "I have printed")

function1('This is me')
print(l)



print('3\n')

def harry():
    x = 20
    def rohan():      #nested fun
        global x      #global x searches globally above def harry() for changing any global x
        x = 28        #and not local x = 20 and thus makes(defines new if not available) a
                      #new global variable which does not affect any other local variable like
                      #that of harry() x = 20, x at both the places below remains 20
    print('before calling rohan()',x)   #:20
    rohan()                             #rohan() function property of harry() function
    print('after calling rohan()',x)    #:20

harry()


print('4\n')

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
        print('after calling rohan()',x)  #this line dont get executed here and

        # rohan()
        print('after calling rohan()',x) #here too  in perspective of line {60} closure rohan()
    rohan()# rohan must be closed in the end in a line vertically parallel to def rohan()
           # and not inside of def rohan() like in line{60}
           # in order to get executed all lines inside of function rohan()

harry()
print(x)

#1: x = 89                                                                  (52}
#2: harry() function runs                                                   {66}
#3 goes into function def harry()[till now local x=20 , global x=89]        {53}
#4:rohan() runs now global value of x changes to 88                         {62}
#5: local value of x=20 that is printed for line 58 and 61                  {58}
#6: global value of x = 88(changed at line 57) so it is printed for line 60.{67}