import  numpy as np
epoch = 1
rate = 0.01
w = np.array([[-0.0,-0.4,-0.4,-0.0]])
X = np.array([[2.8,3.8,5.6,3.1],[2.7,5.7,6.6,7.0],[4.9,5.2,4.8,6.5],[2.1,3.8,2.7,4.2],[5.2,2,4.5,3.9]])
count = 1
while epoch:
    print "epoch: ", count
    count+=1
    epoch-=1
    accchange = 0
    for n in X:

        y = w.dot(n)
        xt_yw = n - y.dot(w)
        rateyx_t = rate*y*xt_yw
        accchange+=rateyx_t
        print y,"    ",xt_yw,"   ",rateyx_t
    w = w+accchange
    print "total weight change: " ,accchange ,"   ",w


#project the zero-mean data on firt principal component
for n in X:
    print w.dot(n)

