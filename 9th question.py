import numpy as np

def pca(X, num_components):
    
    X_centered = X - np.mean(X, axis=0)
    
    
    cov_matrix = np.cov(X_centered, rowvar=False)
    
    
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    
    components = eigenvectors[:, :num_components]
    
    
    explained_variance = eigenvalues[:num_components] / np.sum(eigenvalues)
    
    return components, explained_variance


np.random.seed(0)
X = np.random.rand(100, 2)  

num_components = 1
components, explained_variance = pca(X, num_components)

print("Principal components:")
print(components)
print("Explained variance:", explained_variance)

"""
output:-
Principal components:
[[-0.63106527]
 [ 0.77572974]]
Explained variance: [0.53490112]
"""
