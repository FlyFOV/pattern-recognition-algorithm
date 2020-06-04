import numpy as np
from numpy import linalg as LA
from sklearn.decomposition import IncrementalPCA
X = np.array([[1.,2,3,2],[2,3,5,2],[1,1,1,1]])
m = np.mean(X,axis=1)
X = X.transpose()
for n in X:
    n-=m
X = X.transpose()
#zero mean ,by column
C = X.dot(X.transpose())/4   #column
w,v = LA.eig(C)
# print w
# print v
Vt= np.array([[0.4719 ,0.8817,0],[-0.8817,0.4719,0]])
# print Vt.dot(X)
v = np.array([[-0.05,0.59,0.41,0.7],[0.92,-0.28,0.17,0.2]])
c = np.array([2.8,3.8,5.6,3.1])
print v.dot(c)