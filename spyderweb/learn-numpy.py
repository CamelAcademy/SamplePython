# numpi array are fast, less memory and convenient operations then list
# https://www.youtube.com/watch?v=8JfDAm9y_7s

import numpy as np
import time
import sys
##################################
# a = np.array([(1,2,3),(4,5,6)])
# print(a)
##################################
print("\nMemory Test\nPython List")
s = range(1000)
print(sys.getsizeof(100))
print(len(s))
print(sys.getsizeof(4)*len(s))

print("\nNum Pi Array")
p = np.arange(1000)
print(p.itemsize)
print(p.size)
print(p.size*p.itemsize)
##################################
SIZE = 1000000
L1 = range(SIZE)
L2 = range(SIZE)
start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print ((time.time()-start)*1000)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
start = time.time()
result = A1+A2
print ((time.time()-start)*1000)
#####################################
a =np.array([[1,2,3],(4,5,6)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
######################################## Row2Columns
a =np.array([[1,2,3],(4,5,6)])
print(a)
a = a.reshape(3,2)
print(a)
#####################################Slize and Dicing
print(a[0,1])
print(a[0:,1])
print(a[0:1,1])
###################################
a = np.linspace(1,3,5)
print(a) # will make 5 numbers & 4 intervals between 1 & 3