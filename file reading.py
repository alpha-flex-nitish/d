open('harry.txt')    #the second part of the open fun is in which mode do we want open file
print("A: Char by Char reading1")
f = open('harry.txt')
content = f.read()
print(content)

f.close()     #does nothing here but a good practice




print("\nB:Char by Char reading2")
f = open('harry.txt',"rt")
content = f.read()
print(content)
f.close()






print("\nC:Char by Char reading3")
f = open('harry.txt',"rt")
content = f.read(3)
print(content)

content = f.read(3)   #again reads 3 characters of file
print(content)
f.close()




print("\nD:Char by Char reading4")
f = open('harry.txt',"rt")
content = f.read(34455)
print("1",content)

content = f.read(34455)   # ignored cause no characters let in file
print("2",content)
f.close()





print('\nE: Line by line reading1')
f = open('harry.txt')
#content = f.read()          # whenever we do f.read file pointer becomes empty and next time we iterate (for line in content:)
                                #next time nothing is printed it is already raeden becoz of  content = f.read()
for line in f:
    print(line,end='')
f.close()




print('\n\nF: Line by line reading2')    #star
f = open('harry.txt',"rt")
print(f.readline())      #ouput in new lines cauze its already in file
print(f.readline())
print(f.readline())
#content = f.read()

# for line in f:
#     print(line, end = "")
f.close()


#to store all lines in a list
print('\nG: to store all lines in a list')
f = open('harry.txt',"rt")
print(f.readlines())
f.close()