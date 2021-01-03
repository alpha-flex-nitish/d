#42
import time
initial = time.time()
print(initial)
k = 0

while (k<45):
    print("This is harry bhai")
    k += 1
    time.sleep(0.00000001)
for i in range(45):
    print('This is harry bhai')
print('while loop ran in ',time.time()-initial,'Seconds')

initial2 = time.time()
for i in range(45):
    print('This is harry bhai')
print('For loop ran in', time.time()-initial2,'Seconds')

import time
localtime = time.asctime(time.localtime())
print(localtime)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
