import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X = np.array([[2, 0 ], [0, 3], [3, 3], [0, 5], [3, 1]])
y = np.array([1, 1, 2, 2, 2])
clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
print clf.means_
#change w to get different result
w = np.array([-4,-4])
m1 = clf.means_[0]
m2 = clf.means_[1]
class1 = np.array([[2,0],[0,3]])
class2 = np.array([[3,3],[0,5],[3,1]])
sb = (w.dot(m1-m2))**2
sw = 0
for n in class1:
    sw+=w.dot(n-m1)**2
for n in class2:
    sw+=w.dot(n-m2)**2
print sw
J = sb/sw
print J

#print clf.means_
#print clf.priors_