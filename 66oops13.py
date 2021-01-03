class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(B, C):
    def met(self):
        print("This is a method from class D")

#preference D>B>C>A

#if pass in some of the above class then above preference is pfeferred to print in case of multiple inheritence
a = A()
b = B()
c = C()
d = D()

d.met()




