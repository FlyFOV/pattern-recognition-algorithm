from sklearn.linear_model import Perceptron
import numpy as np
X = np.array([[1,5],[2,5],[4,1],[5,1]])
y = np.array([1,1,2,2])
clf = Perceptron(alpha=1)
clf.fit(X,y)
print clf.coef_


