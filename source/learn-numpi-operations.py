import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3])
print(a.min())
print(a.max())
print(a.sum())

a = np.array([  (1,2,3),
                (4,5,6)])
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))

b = np.array([  (7,6,5),
                (5,6,7)])

print(a+b) # same thing in list we need to use for loop
print(a-b)
print(a*b)
print(b/a)
print(np.vstack((a,b))) # why one extra () ??
print(np.hstack((a,b)))
print(a.ravel()) # make into single file
###########################################
x = np.arange (0,3*np.pi,0.1)
y = np.tan(x)
plt.plot(x,y)
plt.show()
############################################
ar = np.array([1,2,3])
print(np.exp(ar))
print(np.log(ar))
print(np.log10(ar))