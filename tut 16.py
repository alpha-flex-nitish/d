"""list = [2,'li','fi',3,34,'dot',54,'pot',7,6,90,'harry','hat']

   # print(list.items())
#for item in list:

#if (list1.item>6)
# print(list.item)
#else:
   #     print()
"""
#for loops


list1  = ['Harry','Larry','Carry','Marie']
print(list1[0],list1[1])

for item in list1:
    print(item)

#in tuple

list1  = ('Harry','Larry','Carry','Marie')
print(list1[0],list1[1])

for item in list1:
    print(item)

list1 = [['Harry',1],['Larry',2],['Carry',6],['Marie',250]]
for item in list1:
    print(item)

for item,lolypop in list1:
    print(item,'and lolly is',lolypop)

#in dict


dict1 = dict(list1)
print(dict1)

#for item,lolypop in dict1:   # :E
#    print(item,'and lolly is',lolypop)
for item, lolypop in dict1.items():
        print(item, 'and lolly is', lolypop)

for item in dict1:    #to get only keys we can do directly by item in dict1
    print(item)

#Quiz
list = [2,'li','fi',3,34,'dot',54,'pot',7,6,90,'harry','hat']
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)
#print(item)
#for item in list:
   # if str(item).isnumeric()
  #  if (item.isnumeric() and item>6):
     #   print(item)

items = [int, float,"HaERRY",5,3,22,21,64,23,233,23]

for items in items:
    if str(items).isnumeric() and items>6:
        print(items)




