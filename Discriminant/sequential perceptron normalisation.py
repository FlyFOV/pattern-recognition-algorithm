#with augumented notation and sample normalisation
import numpy as np
rate = 1
X = np.array([[1,1,5],[1,2,5],[-1,-4,-1],[-1,-5,-1]])
a = np.array([-25,6,3])
while True:
    count = 0
    #accfix = np.array([0,0,0])
    for n in X:
        g = a.dot(n)
        if g<=0:
            a+=n
        else:
            count+=1
        print g,a
    if count==len(X):
        break

