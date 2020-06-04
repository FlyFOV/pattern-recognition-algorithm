from sklearn.cluster import KMeans
import numpy as np
X = np.array([15.5,10.5,10.5,7.5,6.5,5.5,14.5,13.5])
initial = np.array()
kmeans = KMeans(n_clusters=2).fit(X)
print  kmeans.cluster_centers_
print  kmeans.n_iter_
print kmeans.labels_
