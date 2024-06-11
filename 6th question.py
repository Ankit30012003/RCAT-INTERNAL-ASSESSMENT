import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function(theta, X, y):
    m = len(y)
    h = sigmoid(X.dot(theta))
    cost = -1 / m * (np.sum(y * np.log(h) + (1 - y) * np.log(1 - h)))
    return cost

theta = np.zeros(X.shape[1])
cost = cost_function(theta, X, y)
print("Cost:", cost)

"""
output:-  Cost: 69.31471805599453
"""
