#53
class Student:
    pass            # pass matlab kuch nahi
                    # python me agar hum chahte
                    # hai ki kuch na hi to hum pass likhte hai

harry = Student()
larry = Student()
print(harry, larry)   #do alag alag object at 2 dif  location

harry.name = "Harry"
harry.std = 12
harry.section = 1
print(harry.name,harry.std, harry.section)

larry.std = 9
larry.subjects = ['hindi','physics']
print(larry.std,larry.subjects)
#print(larry.name):E - as no name given to larry









