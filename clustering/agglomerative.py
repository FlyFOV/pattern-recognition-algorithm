from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1,0],[0,2],[1,3],[3,0],[3,1]])
clustering = AgglomerativeClustering().fit(X)
print clustering.labels_
