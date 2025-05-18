import numpy as np
from .layer import Layer

class FCLayer(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5 
        # input*output méretű mátrix [-0.5, 0.5[ közötti számokkal
        self.bias = np.random.rand(1, output_size) - 0.5
        
    def forward_propagation(self, input):
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output