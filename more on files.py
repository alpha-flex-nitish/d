#30
f = open('harry.txt',)
print(f.tell())
print(f.readline())
                           #a = f.write("") :E unsupported with print(f.readline())
                             #  print(a)     in order to get where the pointer is
f.seek(10)               #resets pointer to the given place from where
                            #we want the pointer to start read file
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())


f.close()
