#44
l1 = ['Bhindi', 'Aloo', 'Chopstics', 'chowmein']

i = 1
for item in l1:
    if i%2 is not 0:
        print(item)
    i += 1
print(i)
i = 1
for item in l1:
    if i%2 is not 0:
        print(f'Jarvis Please buy {item}')
    i += 1
print(i)

# reduce above programme :Enumerate fun  : ye index(i) aur item dono deta hai


for index, item in enumerate(l1):       # index starts from zero here
    if index%2==0:
        print(f'Jarvis Please buy {item}')




