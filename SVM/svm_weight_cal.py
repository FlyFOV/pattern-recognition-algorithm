import numpy as np
from sklearn.svm import SVC

X = np.array([[-1,-4],[-2,-9],[3,-9]])
y = np.array([1,1,-1])
clf = SVC(gamma='auto',kernel="linear")
clf.fit(X, y)
print clf.coef_
print clf.intercept_
#only use when linear seperable
#print clf.support_vectors_