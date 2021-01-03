#sets
s = set()
print(type(s))

s_from_list = set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))


#OR same as value of sets now stored in l
l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))

#add elements in blank set s1

s1 = set()
print(s1)

s1.add(1)
print(s1)

s1.add(1)  #list add all values But set append unique values in it as we learnt in mathematics
s1.add(1)
print(s1)

s1.add(1)
s1.add(2)
print(s1)

s1.union({1,2})
print(s1)

s1.union({1,2,3})
print(s1)  # new variable
s2 = s1.union({1,2,3})
print(s2)
s2 = s1.intersection({1,2,3})

print(len(s2))
print(max(s2))
print(min(s1))


s = set()
s1 = {4,6}
print(s.isdisjoint(s1))

s.add(1)
s.add(2)
s.remove(2)
print(s)