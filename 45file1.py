#45
#Import in python

import sklearn as sk   # it has come in current scope: global and not local scope
#h = 1                 #do
print(sk.__version__)

# line2 me jo module inmort karke layega kaha se layega
# kis tarah layega ye jan ne ke liye ek module hota hai

import sys
print(sys.path)   #it searches the module in printed sequence
                  # this checking order can be changed

from sklearn.ensemble import RandomForestClassifier   #RFC-an package in machine learning
print(RandomForestClassifier)
print(RandomForestClassifier())

import file2
#file2.n     E; since variable n is not defined in file2
file2.a
print(file2.a)     # we can acces the variables of file2 by 'file2.a'


#aliter
from file2 import a   #now we need not write file2.a
print(a)              #and can directly acees a from file2

#best way now
import file2
print(file2.a)
file2.printjolke('This is me')

#jab bhi ham koi fun banate hai like 10-15 to
#unko ek file-{here-file2} me rakho aur import karo
#jaha use karna ho

#some variable/classes already in global scope:-
#int ,float ,__name__







