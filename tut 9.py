#LISTS FUN


grocery = ['Harpic','vim bar','deodrant','Bhindi','Lollypop',56]
print(grocery[0])
print(grocery[5])
numbers = [2,7,9,11,3]
print(numbers[2])
#print(numbers.sort())   #:None
numbers.sort()
#print(numbers.sort())  #or
print(numbers)
numbers.reverse()
print(numbers)
#print(numbers[9])  #:E
print(numbers[2])

#SLICING   #slicing returns a list  these are lists [11, 9, 7, 3, 2]


print(numbers[0:5])    #OR
print(numbers[:5])     #OR
print(numbers[:])

print(numbers[1:])    #prints from 1 to 4 except 0
print(numbers[1:4])


#EXTENDED SLICING

print(numbers[::])
print(numbers[::1])  #escapes 1-1 0
print(numbers[::2])
print(numbers[::3])   #dont take negative slicing except -1

print(numbers[::-1])

print(numbers[1:5:2])

print(len(numbers))
print(max(numbers))
print(min(numbers))

#APPEND

numbers = []

numbers.append(7)
numbers.append(71)
numbers.append(71)
numbers.append(71)
print(numbers)

#insert anwhere instead append which only add at end

numbers = [2,7,9,11,3]

numbers.insert(1,67)
print(numbers)
numbers.insert(2,66)

print(numbers)

#remove

numbers.remove(9)
print(numbers)

#pop  last element chopped off

numbers.pop()
print(numbers)






numbers = [2,7,9,11,3]
numbers[1] = 98    # value of number 'list' at 1 changed to 98 instead 7
print(numbers)

#MUTABLE= CAN CHANGE   :LIST IS IT
#IMMUTABLE = CANT CHANGE    :TUPLE IS IT

tp = (1,2,3)
#      tp[1] = 8     :E  # value of tuple cant change
print(tp)

#tp = (1,)  # for 1 value tuple put a comma

#value swap


a = 1
b = 8

#M-1
temp = a
a = b
b = temp
print(a,b)

#M-2

a,b = b,a
print(a,b)

#EXTEND,CLEAR,INDEX,COUNT,COPY


