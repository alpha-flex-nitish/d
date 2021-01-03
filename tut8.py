"""yourstr = ("Harry is a good boy")
print(len(yourstr))
#translation = {97:None,98:None,99: 105}
#print(yourstr.translate())
print(yourstr.casefold())
#   print(yourstr.center()) feed [width."fillchar"} ~
loaf = yourstr.center(33,'z')
print(loaf)
thestr = "dil dheere dheere dhadke aaj hone ko  hai aagaaj"
print(thestr.count("e"))
print(loaf.count("z"))
print(len(thestr))
thenewstr = thestr.center(52,"z")
print(thenewstr.count("z"))
print(thestr.encode())
print(yourstr.encode())
y = yourstr.encode()
#print(y)
#print(ystr.encode())                               nw
#print(ystr.encode(ystr.encode()))                  nw
print(yourstr.endswith("boy"))
ystr = 34
#print(ystr.endswith("34"))
mystr = "my age is 20"
print(mystr)
print("1",mystr.endswith(""))
print(mystr.endswith())
"""
"""
#print("Hello")
#print("H e l l o")



txt = "H\te\tl\tl\to"

print(txt.expandtabs())    # inserts 7 spaces
print("\n")

print(txt.expandtabs(5*1))  # inserts 1 space in b/w of each place where \t is put
print(txt.expandtabs(2))  # inserts 1 space
print(txt.expandtabs(3))  # inserts 3 space
print(txt.expandtabs(4))  # inserts 3 space
print(txt.expandtabs(5))  # inserts 4 space
print(txt.expandtabs(6))  # inserts 5 space
print(txt.expandtabs(7))  # inserts6 6 space
print(txt.expandtabs(8))  # inserts 7 space
print(txt.expandtabs(9))  # inserts 8 space
print(txt.expandtabs(10))  # inserts 9 space
print(txt.expandtabs(11))  # inserts 10 space
print(txt.expandtabs(12)) # inserts 11 space
"""


"""
#  find and index  string

txt = "Hello, welcome to my world."

print(txt.find("q"))    #:-1
print(txt.find('d'))    #:25
print(txt.find('.'))    #:26
print(txt.find('f'))    #:-1
print(txt.find('o'))    #:4
print(txt.index('o'))    #:4 # we can get only first value of position with find and index
print(txt.find('o',6,   12))      #:11
print(txt.find('o',6,11))   #:-1 # not found inside of start and end values so  -1
print(txt.find('w',5,25))    #:7 # can not write 005 or 0025 or 025 in place of 5 and 25
#print(txt.find('e', , ))      # error the print(txt[::1]) or print(mystr[0:n:] technique does not work here

#print(txt.find('o',,))
print(txt.index('y',12,20))    #:-1


print(txt.index("q"))

"""
"""


#ISALPHA  ISALNUM  ISDIGIT   COMPARISION



mystr = 'HrarryIsAGoodBoy'
print(mystr.isalpha(),'\n')

mystr = 'HARRYISONEGOODBOY'
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.isdigit(),'\n')

mystr = '२०१९'
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.isdigit(),'\n')

mystr = 'खूबसूरत'
print(mystr
       .
        isalpha())
print(mystr.isalnum())
print(mystr.isdigit(),'\n')

mystr = '☮'
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.isdigit(),'\n')
"""
"""


#ISDECIMAL STRING



mystr = '4.5'
print(mystr.isdecimal())

mystr = '4'
print(mystr.isdecimal())

mystr = '4,5'
print(mystr.isdecimal())

mystr = '4/5'
print(mystr.isdecimal())

mystr = '4.5'
print(mystr.isdecimal())

mystr = '5/5'
print(mystr.isdecimal())

mystr = '4-5'
print(mystr.isdecimal())

mystr = '4-5'
print(mystr.isdecimal())

mystr = '5-5'
print(mystr.isdecimal())
"""
"""

#ISDIGIT STRING


mystr = '3²'
print(mystr.isdigit())

mystr = '(3²)'
print(mystr.isdigit())

mystr = '02²'
print(mystr.isdigit())

mystr = '0.2²'
print(mystr.isdigit())

mystr = '(1.0)²'
print(mystr.isdigit())

mystr = '8²'
print(mystr.isdigit())

mystr = '0²'
print(mystr.isdigit())

mystr = '0.0²'
print(mystr.isdigit())

mystr = '(8*9)'
print(mystr.isdigit())

mystr = '8+9'
print(mystr.isdigit())

mystr = '858499'
print(mystr.isdigit())

mystr = '[858499]'
print(mystr.isdigit())


"""
"""

# ISIDENTIFIER STRING


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
e = "my_demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())
"""
"""

# ISLOWER STRING


txt = "hello 1_ world!"

x = txt.islower()

print(x)

"""
"""



#   ISNUMERIC   STRING




txt = "565543"
print(txt.isnumeric())   #T


txt = "5655 43"
print(txt.isnumeric())   #F


txt = "565_543"
print(txt.isnumeric())   #F


txt = "5655+43"
print(txt.isnumeric())   #F


txt = "5*6"
print(txt.isnumeric())


txt = "56.5543"
print(txt.isnumeric())   #F


txt = "565543A"
print(txt.isnumeric())   #F


txt = "a565543"
print(txt.isnumeric(),'\n')   #F



mystr = '3²'
print(mystr.isnumeric())  #T

mystr = '(3²)'
print(mystr.isnumeric())   #F

mystr = '02²'
print(mystr.isnumeric())   #T

mystr = '0.2²'
print(mystr.isnumeric())   #F

mystr = '(1.0)²'
print(mystr.isnumeric())   #F

mystr = '8²'
print(mystr.isnumeric())   #T

mystr = '0²'
print(mystr.isnumeric())   #T

mystr = '0.0²'
print(mystr.isnumeric())   #F

"""


#    ISPRINTABLE      STRING


"""


txt = "Hello!\nAre you #1?"

print(txt.isprintable())



txt = "Hello!\rAre you #1?"

print(txt.isprintable())



txt = "Hello!\tAre you #1?"

print(txt.isprintable())



txt = "Hello!\\\\Are you #1?"

print(txt.isprintable())



txt = "Hello!Are you #1?  AND  !@$%^&*(),.<> 0.2²(0.2)²"

print(txt.isprintable())


"""

"""
#  ISSPACE   STRING


txt = "   "

print(txt.isspace())


txt = " \\  "

print(txt.isspace())


txt = "  \v "

print(txt.isspace())


txt = "\r"

print(txt.isspace())

txt = "\n"

print(txt.isspace())

txt = "  \a  \b  \f   \n  \r  \t  \v "

print(txt.isspace())

"""

"""
#  ISTITLE



a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
e = "Hello And Welcome To My World"
f = "Hello ANd Welcome To My World"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
print(e.istitle())
print(f.istitle())

"""


#   ISUPPER


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

