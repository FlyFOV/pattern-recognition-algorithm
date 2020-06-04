import  numpy as np
rate = 1
theta = 1
w1 = -1
w2 = -1.5
w = np.array([-theta,w1,w2])

#augmented data , first element is 1
x = np.array([[1,-1,0],[1,1,-1],[1,0,-1]])
t = [1,0,0]
epoch = 1
while True:
    print "epoch: ",epoch
    count = 0
    tolc = [0,0,0]
    for i,n in enumerate(x):
        if w.dot(n)==0:
            y = 0.5
        elif w.dot(n)<0:
            y = 0
        else:
            y=1
        #y = 0 if w.dot(n) <=0 else 1
        t_y = t[i] - y
        if t_y == 0:
            count+=1
        rt_yxt = rate*(t_y)*n
        tolc += rt_yxt
        print t_y ,"  " ,rt_yxt,w
    w = w + tolc
    print "total weight change: ",tolc,"    ",w
    epoch+=1
    if count== len(t):
        break