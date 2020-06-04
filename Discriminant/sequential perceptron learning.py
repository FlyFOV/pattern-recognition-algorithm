#without norm
import numpy as np
#augumented data
X = np.array([[1.,0,2],[1,1,2],[1,2,1],[1,-3,1],[1,-2,-1],[1,-3,-2]])
y = np.array([1,1,1,-1,-1,-1])
a = np.array([1,0,0])

while True:
    count = 0
    for i,n in enumerate(X):
        aold = a
        g = a.dot(n)

        w = 1 if g>=0 else -1
        if w!= y[i]:
            a = a+y[i]*n
        else:
            count+=1
        print aold,"  ",n,"   ",g,"   ",a
    if count==len(X):
        break