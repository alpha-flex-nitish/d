#65
# super and overiding
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
class B(A):0
    classvar2 = "I am in class B"
a = A()
b = B()
print(1,b.classvar1)
#####################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"        ##
class B(A):
    classvar2 = "I am in class B"
a = A()
b = B()
print(2,b.classvar1)
#####################
class A:
    classvar1 = "I am a class in variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
class B(A):
    classvar1 = "I am in class B"                  ##     (hala kioverwrite kar diya hai??3:26)
a = A()
b = B()
print(3,b.classvar1)#search instance 1st
#####################
class A:
    classvar1 = "I am a class in variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
                                                          ##
class B(A):
    classvar1 = "I am in class B"
a = A()
b = B()
print(4,b.classvar1)
######################
class A:
    classvar1 = "I am a class in variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
class B(A):
    pass                                                  ##
a = A()
b = B()
print(5,b.classvar1)
#######################
#ovariding finished

#now method overiding

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"        ##
class B(A):
    classvar1 = "I am in class B"#(attribute ovaride)       ##
    def __init__(self):#(constractor ovaride)               ##
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
a = A()
b = B()
print(6,b.classvar1)
########################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):#These 3 lines ignored bye mathod ovaride// only child mathod considered
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):#(mathod ovarided) and dad wala method ignored
        self.var1 = "I am inside class B's constructor"
                                                        ##
a = A()
b = B()
print(7,b.classvar1)
########################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()                          ## used for taking methadA in consider wapis se and we used it to call special rest is same when it is above every argument in method.
        self.var1 = "I am inside class B's constructor"
a = A()
b = B()
print(8,b.special,"\n ",b.var1,"\n ",b.classvar1)
#print(8,b.special,"\n ",a.classvar1,"\n ",b.classvar1,"\n ",a.var1,"\n ",b.var1)
#############################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"      ##
a = A()
b = B()

print(9,b.special,"\n ",b.var1,"\n ",b.classvar1)
# print(9,b.special,"\n ",a.classvar1,"\n ",b.classvar1,"\n ",a.var1,"\n ",b.var1)
#############################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self): #1
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self): #2
                                                    ##
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__() #3                       ##
a = A()
b = B()
print(10,b.special,"\n ",b.var1,"\n ",b.classvar1)
# print(10,b.special,"\n ",a.classvar1,"\n ",b.classvar1,"\n ",a.var1,"\n ",b.var1)

#pahle #1 run fir #2 run fir #3 ke karan #1 run
##############################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(11,super().classvar1)                     ##
a = A()
b = B()
print(" ",b.special,"\n ",b.var1,"\n ",b.classvar1)
###############################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()                              ##
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        print(12,super().classvar1)
a = A()
b = B()
print(" ",b.special,"\n ",b.var1,"\n ",b.classvar1)
# print(" ",a.classvar1)
###############################
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constractor"
        self.classvar1 = "Instance var in class A"
        self.special = "special in constractor A"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()                              ##
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        print(13,super().classvar1)
        # print(" ",super().var1)# E== print(super()._______) only calls class variable not instances
a = A()
b = B()
print(" ",b.special,"\n ",b.var1,"\n ",b.classvar1)

# Agar hm class b ke ander constructor nhi bnate to
# instance variable kaha se aa rha b me?
#incnonclusion
##
#do baatein:
#1:super() ka matlab pahle super ( parent class) me jao fir mere niche jana
#2:print(11,super().classvar1): ye sirf parent class se class variable dega samjhlo and na ki parent class se instance var





#Called as - super class ka constructor
# super().__init__()
# #isa
# super(B, self).__init__()
#inka matlab pahle super  me jao fir mere niche jana
#super() ka matlab pahle super (babuji) me jao fir mere niche jana


























# Rough
# class A:
#     classvar1 = "I am a class variable in class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constractor"
#         self.classvar1 = "Instance var in class A"
#         self.special = "special in constractor A"
# class B(A):
#     classvar1 = "I am in class B"
#         print(13,super().classvar1)
# a = A()
# b = B()
# print(" ",b.special,"\n ",b.var1,"\n ",b.classvar1)
# Agar hm class b ke ander constructor nhi bnate to
# 1)instance var in class B
# 2)instance var in class A
# 3)class var in class B
# 4)class var in class A
#  Ye order chall ra hai
# But constructor bna dene ke baad agar constructor me sirf pass likh do to order change ho ra hai ,
# 1) instance var in class B
# 2) class var in class B
# 3)class var in class A
# And it don't consider instance var in class A .if I comment class var in A and B class but instance var in class A exists, still it gives me error
# 'B' object has no attribute 'classvar1'.
# I can't understand why.
# Anybody please explain
# super().__init__() ye kahi bhi ho
#         once this:    print(11,super().classvar1)
#                             is called tab sirf super class ka claas variable print hoga naa ki super class ka instance variable
#                             bhale hi us naam ka varible methad ke andar hi kyu na ho as instance variable
#                             aur agar once this is written aur super class ke paas iss naam ka class variable na ho to error aa jayega
#                             bhale hi usi naam ka variable uske yani ki super class ke instance me hi kyu na majood ho.














































































class A:
    classvar1 = "I am a class in variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
class B(A):
    classvar1 = "I am in class B"
    # def __init__(self):
    #     self.var1 = "I am inside class B's constructor"
    #     self.classvar1 = "Instance var in class B"
a = A()
b = B()
print(b.classvar1)