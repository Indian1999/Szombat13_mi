import numpy as np

def mse(y_expected, y_predicted):
    return np.mean((y_expected - y_predicted) ** 2)

def mse_deriv(y_expected, y_predicted):
    return 2 * (y_expected - y_predicted) / y_expected.size