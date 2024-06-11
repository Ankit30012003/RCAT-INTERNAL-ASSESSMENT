import numpy as np

class KMeans:
    def fit(self, X, n_clusters, max_iter=300):
        centroids = X[np.random.choice(X.shape[0], n_clusters, replace=False)]

        for _ in range(max_iter):
            labels = self._assign_clusters(X, centroids)
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(n_clusters)])

            if np.allclose(centroids, new_centroids):
                break

            centroids = new_centroids

        return labels, centroids

    def _assign_clusters(self, X, centroids):
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        return np.argmin(distances, axis=0)

np.random.seed(0)
X = np.random.rand(100, 2)

kmeans = KMeans()
labels, centroids = kmeans.fit(X, n_clusters=3)

print("Cluster labels:", labels)
print("Final centroids:", centroids)

"""
output:-
Cluster labels: [2 0 2 2 0 0 2 1 2 2 0 2 2 2 0 2 2 2 0 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 0 0
 0 1 1 1 2 0 1 2 2 2 1 1 0 0 2 2 0 2 2 0 0 0 0 0 0 2 1 0 0 1 0 2 0 0 2 0 2
 2 2 2 2 0 1 0 2 0 1 0 1 1 0 2 0 2 0 0 2 0 1 2 0 1 1]
Final centroids: [[0.76167338 0.40765364]
 [0.27223715 0.21097997]
 [0.35217863 0.78488734]]
 """
