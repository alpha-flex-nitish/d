#DICTIONARY
#dictionary is key value pair

d1 = {}
print(type(d1))  #:<class 'dict'>

d1 = []
print(type(d1))    #:<class 'list'>


d1 = ()
print(type(d1))     #:<class 'tuple'>


d1 = {}

d2 = {'Harry':"Burger",
      'Rohan':'Fish','SkillF':'Roti'}

print(d2['Harry'])
print(d2['Rohan'])


d2 = {'Harry':"Burger",
      'Rohan':'Fish','SkillF':'Roti',
      'Shubham':{'B':'maggie','L':'roti','D':'Chicken'}}
print(d2['Shubham'])

#Add value to dict
d2['Ankit'] = 'Junk Food'
print(d2)

d2['Auranzeb'] = 'Kebabs'
print(d2)

d2['420'] = 'Kebabs'
print(d2)

del d2['420']
print(d2)

print(d2.copy())

d3 = d2     #d3 is referred to d2; no new d3 dict formed
del d3['Harry']  # so deleted from both d2 &d3
print(d2)

d3 = d2.copy()   #d3 is a new copy of d2 now d2 remains safe
del d3['Rohan']
print(d2)
print(d3)

print(d2.get('SkillF'))

print(d2.update({'Leena':'Toffee'}))
print(d2)


#two ways of updating:
#d2['Ankit'] = 'Junk Food'
#print(d2.update({'Leena':'Toffee'}))

print(d2.keys())
print(d2.items())  #prints key, items pairs

#<<<