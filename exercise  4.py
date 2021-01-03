#29
#pattern printing
# Input = Integer n
# Boolean = True or False
#
# True n=4
# *
# **
# ***
# ****
#
# False
# ****
# ***
# **
# *
i = 1
in1 = 1
print('Enter a number for height of rows ')
n = int(input())
print('enter 1 for ascending and 0 for descending ')
b = int(input())
if(b):
    while (i <= n):
        print(i * '*')
        i = i + 1
elif(b ==False):
    while (n >= 0):
        print(n * '*')
        n = n - 1


# f = open('harryfood.txt','r+')
# print(f.read())
# f.write("kanda")