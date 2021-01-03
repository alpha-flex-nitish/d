#47
#join function
lis = ['John', 'cena', 'Randy', 'orton',
       'sheamus', 'khali', 'jinder mahal']
print(1)
for item in lis:
    print(item, 'and', end = ' ')

print('\n',2)
a = ' and '.join(lis)
print(a,'other wwe superstars')

print(3)
a = ', '.join(lis)
print(a,'and other wwe superstars')