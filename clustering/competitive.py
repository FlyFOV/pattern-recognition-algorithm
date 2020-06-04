import numpy as np
X = np.array([[1.,0.],[0,2],[1,3],[3,0],[3,1]])
iter = 5
w = np.array([[1.,1.],[2,2]])
rate = 0.5
for i in range(iter):
    d_0 = np.linalg.norm(X[i]- w[0])
    d_1 = np.linalg.norm(X[i] - w[1])
    minnum = 0 if d_0<d_1 else 1
    w[minnum] = w[minnum] + rate*(X[i] - w[minnum])
    print d_0," ",d_1,"  ",w[minnum]
#use the new w to classify
print "now classify"
for i in range(iter):
    d_0 = np.linalg.norm(X[i]- w[0])
    d_1 = np.linalg.norm(X[i] - w[1])
    minnum = 1 if d_0<d_1 else 2
    print d_0,"     ",d_1,"     ",minnum

