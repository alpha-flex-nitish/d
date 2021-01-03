# class A:
#     classvar1 = "Class var in A"
#     def __init__(self):
#         self.var = "Class A constructor"
#         self.classvar1 = "Instance var in A"
# class B(A):
#     def __init__(self):
#         self.var1 = "Class B constructor"
#         self.classvar1 = "Instance var in B"
#
# a = A()
# b = B()
#
# print(b.classvar1)


class A:
    classvar1 = "Class var in A"
    def __init__(self):
        self.var1 = "Class A constructor"
        self.classvar1 = "Instance var in A"
class B(A):
    classvar1 = "Class var in B"
    # def __init__(self,aname):
    #     # self.var = "Class B constructor"
    #     # self.classvar1 = "Instance var in B"
    #     pass
a = A()
c = A()
b = B()
# d = =B():E expected aname in ()
# b = B("B's 1st instance")

print(b.classvar1)

