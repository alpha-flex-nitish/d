#32
#Health Management System
#3 - clients - Harry, Rohan, Harsad
#write a fun to lock or retrieve or lock data and their times
def getdate():
    import datetime
    return datetime.datetime.now()
# Total 6 files
# write a fun that when executed takes as input client name
print('Enter 1 To lock data\n'
      'Enter 2 to Retrieve data')
lockorretrieve = int(input())

print('Select 1 for Harry\n'
      'Select 2 for Rohan\n'
      'Select 3 for Harsad')
person = int(input())

print('Select 1 for Food\n'
      'Select 2 for Exercise')
foodorexecise = int(input())

# def getdate():
#     import datetime
#     return datetime.datetime.now()
# print('Date and Time:', getdate())


if(lockorretrieve == 2):
    if(person == 1):
        if(foodorexecise == 1):
            f = open('harryfood.txt')
            a = f.read()                                 #() is must after f.read to print opened file
            print(a)
            f.close()
        elif(foodorexecise == 2):
            with open('harryexercise.txt') as f:          #f can be replaced by op dp cp cff
                a = f.read()
                print(a)
    elif (person == 2):
        if (foodorexecise == 1):
            with open('rohanfood.txt.py') as f:
                a = f.read()
                print(a)
        elif(foodorexecise == 1):
            with open('rohanexercise.txt.py') as f:
                a = f.read()
                print(a)
    elif (person == 3):
        if (foodorexecise == 1):
            with open('harshadfood.txt.py') as f:
                a = f.read()
                print(a)
        elif (foodorexecise == 1):
            with open('harshadexercise.txt.py') as f:
                a = f.read()
                print(a)

elif(lockorretrieve == 1):
    if (person == 1):
        if (foodorexecise == 1):
            f = open('harryfood.txt',"r+")
            # a = f.read()
            # print(a)
            print(f.read())
            print('enter diet')
            def getdate():
                import datetime
                return datetime.datetime.now()
            takedate = str(getdate())
            #print(takedate[:19:])
            print('[ Date and Time:',takedate[:19:],"]")
            food = input()
            f.write(takedate[:19:])
            f.write("\n")
            f.write(food)
            f.write("\n\n")
            f.close()
        elif (foodorexecise == 2):
            f = open('harryexercise.txt', "r+")
            print(f.read())
            print('enter exercise')
            def getdate():
                import datetime
                return datetime.datetime.now()
            takedate = str(getdate())
            print('[ Date and Time:',takedate[:19:],"]")
            exercise = input()
            f.write(takedate[:19:])
            f.write("\n")
            f.write(exercise)
            f.write("\n\n")
            f.close()
    elif (person == 2):
        if (foodorexecise == 1):
             f = open('rohanfood.txt.py', "r+")
             print(f.read())
             print('enter diet')
             def getdate():
                 import datetime
                 return datetime.datetime.now()
             takedate = str(getdate())
             print('[ Date and Time:', takedate[:19:], "]")
             food = input()
             f.write(takedate[:19:])
             f.write("\n")
             f.write(food)
             f.write("\n\n")
             f.close()
        elif (foodorexecise == 2):
            f = open('rohanexercise.txt.py', "r+")
            print(f.read())
            print('enter exercise')
            def getdate():
                import datetime
                return datetime.datetime.now()
            takedate = str(getdate())
            print('[Date and Time:', takedate[:19:], "]")
            exercise = input()
            f.write(takedate[:19:])
            f.write("\n")
            f.write(exercise)
            f.write("\n\n")
            f.close()
    elif (person == 3):
        if (foodorexecise == 1):
            f = open('harshadfood.txt.py', "r+")
            print(f.read())
            print('enter diet')
            def getdate():
                import datetime
                return datetime.datetime.now()
            takedate = str(getdate())
            print('[ Date and Time:',takedate[:19:],"]")
            food = input()
            f.write(takedate[:19:])
            f.write("\n")
            f.write(food)
            f.write("\n\n")
            f.close()
        elif (foodorexecise == 2):
            f = open('harshadexercise.txt.py', "r+")
            print(f.read())
            print('enter exercise')
            def getdate():
                import datetime
                return datetime.datetime.now()
            takedate = str(getdate())
            print('[Date and Time:', takedate[:19:], "]")
            exercise = input()
            f.write(-takedate[:19:])
            f.write("\n\n")
            f.write(exercise)
            f.write("\n")
            f.close()

# def getdate():
#     import datetime
#     return datetime.datetime.now()
# takedate = str(getdate())
# print(takedate[:19:])
#     #print('[Date and Time:', getdate[:10:], "]")

# with open('harryfood.txt') as f:
#     a = f.read
#     print(a)
#