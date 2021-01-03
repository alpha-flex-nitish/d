#40
#Sanke Water Gun
n = 1
winc =0
winm =0
import random

# list = ['snake','water', 'gun']
# dict = {'1:snake','2:water', '3:gun'}
# choice = random.choice(list)
# print('Select S for Sanke\n'
#       'Select W for Water\n'
#       'Select G for Gun')
# i = input()
# print(choice)

while(n<=10):
    print('Turn',n)
    list = ['Snake', 'Water', 'Gun']
    Compchoice = random.choice(list)
    print('Select s or 1 for Sanke\n'
          'Select w or 2 for Water\n'
          'Select g or 3 for Gun')
    i = input('Your choice-',)
    print('Comp choice-',end='')
    print(Compchoice)
    print('\n')
    if (i == 's' or i=='1'):
        if (Compchoice == 'Snake'):
            winc = winc + 0
        elif (Compchoice == 'Water'):
            winm = winm + 1
        elif (Compchoice == 'Gun'):
            winc = winc + 1

    elif (i == 'w' or i=='2'):
        if (Compchoice == 'Snake'):
            winc = winc + 1
        elif (Compchoice == 'Water'):
            winc = winc + 0
        elif (Compchoice == 'Gun'):
            winm = winm + 1

    elif (i == 'g' or i =='3'):
        if (Compchoice == 'Snake'):
            winm = winm + 1
        elif (Compchoice == 'Water'):
            winc = winc + 1
        elif (Compchoice == 'Gun'):
            winc = winc + 0
    n = n +1
    print('YourPoint:',winm)
    print('CompPoint:',winc)
    print('\n')
if(winc>winm):
    print('you lose')
elif(winc==winm):
    print('draw')
elif(winc<winm):
    print('you won')


import sys
# sys.exit()
print("Type 'exit' to exit")
response = input()
if response == "exit":
    print("Exiting the program")
    sys.exit()
print("You typed", response)

# i = input()
# if(i=='f'):
#     print('yes')
# elif(i=='F'):
#     print('no')
#f is not same as F
#OR S!=s, W!=, G!=g

# while(n<=10):
#     if()