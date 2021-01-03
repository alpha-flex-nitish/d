import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1['age']
print(a)

#Import only person1 dictionary from the module

from mymodule import person1

print (person1["age"])

#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

#Built-in Modules
import platform

x = platform.system()
print(x)

##dir() function
#lists allfunction name in a module

import platform

x = dir(platform)
print(x[0:4:1])
print(x[74])

from emoji import emojize
print(emojize(':thumbs_up:'))     #'' doesnot work here "" ok
print(emojize(":shipit:"))
print(emojize(":thumbs_up:"))
# print(emoji.emojize(":thumbs_up:"))
                                    #print(emojize[5:9:6]) :E
# import emojis
# emojified = emojis.encode("There is a :snake: in my boot !")
# print(emojified)

import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :blue_heart:"))
print(emoji.emojize("Python is fun :dizzy:"))
print(emoji.emojize("Python is fun :horse:"))
print(emoji.emojize("Python is fun :clock230:"))
print(emoji.emojize("Python is fun :one:"))
print(emoji.emojize("Python is fun :in:"))
print(emoji.emojize("Python is fun :ind:"))
print(emoji.emojize("Python is fun :indi:"))
print(emoji.emojize("Python is fun :india:"))
print(emoji.emojize("Python is fun :trophy:"))
                #pip install emoji
                #pip install emoji --upgrade



                #pip install antigravity
                #pip uninstall antigravity


#To exit
# import sys
# # sys.exit()
# print("Type 'exit' to exit")
# response = input()
# if response == "exit":
#     print("Exiting the program")
#     sys.exit()
# print("You typed", response)

# # Turtle to draw a spiral
# import turtle
#
# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()


# # Turtle to draw a spiral
# def drawSpiral(myTurtle, linelen):
#     myTurtle.forward(linelen)
#     myTurtle.right(90)
#     drawSpiral(myTurtle, linelen - 10)
#
#
# drawSpiral(myTurtle, 80)
# myWin.exitonclick()
                    #pip install colorama
from colorama import Fore, Back, Style

print(Fore.YELLOW)
print('This is a warning!')
#print(Fore.LIGHTRED_EXRED)
print(Fore.RED)
print("dama dama dama")
print(Style.RESET_ALL)    #reset color
print('OM NAMAH SHIVAYA')

                    #pip install tqdm

# import tqdm     star
# from tqdm import trange
# for i in trange(100):
#     sleep(0.01)











