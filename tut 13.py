

var1 = 6
var2 = 56

var3 = int(input())

if var3>var2:          # colon: for mai is if statement ke andar ghusna chahta hu
    print('Greater')   # 4 space called indentation
if var3==var2:
    print('Equal')     #even if 1st if is true, it still checks all if upto last and else
else:
    print('Leser')


if var3>var2:          #first checks if if true bahar aa jayega pure if elif else se
    print('Greater')   #but agar false hua to check elif and if true bahar aajeyga
elif var3==var2:       #but agar false hua to check else
    print('Equal')     #conclusion: Doesnot check all statements.only check until true
else:
    print('Leser')

list1 = [5,7,3]
print(5 in  list1)
print(15 in list1)
if 5 in list1:              # if 5 in list returns true and goes inside if;prints given line
    print('Yes its in the list1')
if 15 in list1:             # if 15 in list returns false dont go inside if;dont print given line
    print('No its not in the list1')
if 15 not in list1:         # if 5 in list returns true and goes inside if;prints given line
    print('No its not in list1')

#Quiz

print('Enter Your Age')

inpage = int(input())

if inpage>18:
    print('You Can Drive')

elif inpage==18:
    print('Come See Us')

else:
    print('No You Are Not Elegible To Drive')