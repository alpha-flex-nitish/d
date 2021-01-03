#31
f = open('harry.txt')
print(f.readlines())
print(f.readline())

#treating file with with block

#This
#with open('harry.txt') as f:

    #is same as :-
#f = open('harry.txt','rt')

#f.close()
#This whole
with open('harry.txt') as f:
    a = f.read(4)
    print(a)

with open('harry.txt') as f:
    a = f.readlines()
    print(a)
#Question of the day :- will the following code read even
# after we already tead with 'with open () as f:'
#Yes or No and why
#Yes because with opn as f: closed the file after reading even after full reading
#so we can read the file by opening it again
f = open('harry.txt')
a = f.read(15)
print(a)
f.close()
