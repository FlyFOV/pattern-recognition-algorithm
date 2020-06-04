import numpy as np
from copy import copy, deepcopy
a = np.array([[-0.5,2,1.5],[-3,-0.5,1],[0.5,1.5,-0.5]])
X = np.array([[1.0,0,1],[1,1,0],[1,0.5,1.5],[1,1,1],[1,0,0]])
#augmented
y = np.array([1,1,2,2,3])
rate = 1

#while True:
for _ in range(5):
    count = 0
    for i,n in enumerate(X):
        res = []
        aold = deepcopy(a)
        maxindex = 0
        maxnum = -1000
        for j in range(3):
            g = a[j].dot(n)
            res.append(g)
            if g > maxnum:
                maxnum = g
                maxindex = j
        if maxindex!=y[i]-1:
            a[maxindex]-=rate*n
            a[y[i]-1]+=rate*n
        else:
            count+=1
        print aold,"   ",n,"   ",res,"    ",y[i]
    # if count==len(X):
    #     break





