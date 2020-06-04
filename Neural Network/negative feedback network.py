import numpy as np
alpha = 0.25
W = np.array([[1,1,0],[1,1,1]])
iteration = 4
x = np.array([1,1,0])
y = np.array([0,0])
for _ in range(iteration):
    wty = y.dot(W)
    et = x - wty
    wet = W.dot(et)
    y = y +alpha*wet
    print et,"    ",wet,"   ",y,"    ",wty

