import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1 - tanh(x)**2

def relu(x):
    return np.maximum(0, x)

def relu_deriv(x):
    return (x>0).astype(x.dtype)