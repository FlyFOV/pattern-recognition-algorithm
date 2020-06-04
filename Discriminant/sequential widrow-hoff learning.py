import numpy as np
#augumented data
X = np.array([[1.,0,2],[1,1,2],[1,2,1],[-1,3,-1],[-1,2,1],[-1,3,2]])
a = np.array([1,0,0])
b = np.array([1.0,1,1,1,1,1])
rate = 0.1
ite = 12
count = 0
while count<ite:
    for i,y in enumerate(X):
        count+=1
        aold = a
        aty = a.dot(y)
        a = a + rate*(b[i]-aty)*y
        print aold,"  ",aty,"   ",a
