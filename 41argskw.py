#41
def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)

function_name_print('Harry','Rohan','Skillf','Harshad',4)   # The no. of variables in line2 must be equal to this line arguments
function_name_print('Harry','Rohan','Skillf','Harshad','Shivam') #not less niether more

print(2)
def funargs(*args):
    print(type(args))
    print(args[0])
har = ['Harry','Rohan','Skillf','Harshad','Shivam']
#har = ('Harry','Rohan','Skillf','Harshad','Shivam') same as above

funargs(*har)
print(3)

def funargs(*args):
    for item in args:
        print(item)
har = ['Harry','Rohan','Skillf','Harshad','Shivam']
#har = ('Harry','Rohan','Skillf','Harshad','Shivam') same as above

funargs(*har)

print(4)

def funargs(normal,*argsrohan , **kwargs ):   #first normal 2nd args 3rskwargs (kwargs or kwargsamul)
    print(normal)                  #*args and **kwargs can be removed without error
    for item in argsrohan:    #*argsrohan E
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key},{value}")


har = ['Harry','Rohan','Skillf','Harshad']
normal = 'I am a normal Argument and the students are:'
funargs(normal, *har)    #*har is args
#kw = {"Rohan:Monitor", "Harry:Fitness Instructor", "The Programmer:Coordinator", "Shivam: Cook"}  :E    #{}
kw = {'Rohan':'Monitor', 'Harry':'Fitness Instructor', 'The Programmer':'Coordinator', 'Shivam': 'Cook'}  #'Rohan:Monitor' wrong error
#kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
 #     "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)


