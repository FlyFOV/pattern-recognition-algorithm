import  numpy as np
rate = 1
theta = -1
w1 = 3
w2 = 0.5
w = np.array([-theta,w1,w2])

#augmented data , first element is 1
x = np.array([[1,2,-1],[1,-1,0],[1,0,0],[1,1,1],[1,0,-1]])
t = [0,1,1,0,1]

while True:
    count = 0
    for i,n in enumerate(x):
        y = 0 if w.dot(n) <0 else 1
        t_y = t[i] - y
        if t_y == 0:
            count+=1
        rt_yxt = rate*(t_y)*n
        w = w+rt_yxt
        print t_y ,"  " ,rt_yxt,w
    if count== len(t):
        break