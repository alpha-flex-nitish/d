#28
f = open('harry.txt','w')        #file handle: returns open also called file pointer
f.write('Harry bhai bahut acche hain')# Everytime we run this programme, everytime the content
                                      #of harry.txt gets replaced by the above f.write line
f.close()

f = open('harry.txt','w')
f.write('Harry bhai bahut acche hain')
f.close()

f = open('harry2.txt','a')              # Everytime we run this programme, everytime the content
f.write('Harry bhai bahut acche hain') #of harry.txt gets append by the abov777777777e f.write line
f.close()
f = open('harry2.txt','a')
f.write('Harry bhai bahut acche hain\n')
f.close()

f = open('harry2.txt','a')
f.write('Harry bhai bahut acche hain\n')
f.close()
f = open('harry2.txt','a')
f.write('Harry bhai bahut acche hain\n')
f.close()
f = open('harry2.txt','a')
f.write('Harry bhai bahut acche hain\n')
f.close()                                #every programme with this append code gets appended despite being
                                         #appended already whenever we run programme,so we need not write again
                                        #same code just run the programme again




#to find how many character did we write in file;(return value)
f = open('harry2.txt', 'a')
a = f.write('Harry bhai bahut acche hain\n')
print(a)
f.close()

f = open('harry2.txt', 'w')                  # write mode matlab jo bhi likha hai usko saaf
a = f.write('Harry bhai bahut acche hain\n')      #kardo aur jo ab likha ja raha hai usko rakho
print(a)                                     #append mode matlab jo file me hai usko to rakho
f.close()                                         #hi rakho aur uske baad me ye jod do


f = open('harry.txt','a')
a = f.write('Harry bhai bahut acche hain\n')
print(a)
f.close()




#Handle to read and write both
f = open('harry2.txt','r+')
print(f.read())
f.write('thank you')