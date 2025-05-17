import numpy as np # terminálba: pip install numpy
import matplotlib.pyplot as plt

class NeuralNetwork():
    def __init__(self):
        self.weights = np.random.random((3, 1)) * 2 - 1
        self.bias = -1
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_deriv(self, x):
        return x * (1 - x)
    
    def train(self, train_x, train_y, epoch):
        history = []
        for i in range(epoch):
            output = self.predict(train_x)
            error = train_y - output
            adjust = np.dot(train_x.T, error * self.sigmoid_deriv(output))
            self.weights += adjust
            print(f"{i+1}. epoch:")
            print(f"\tError: {error.flatten()}")
            print(f"\tAdjust: {adjust.flatten()}")
            print(f"\tWeigths: {self.weights.flatten()}")
            print(f"\tLoss: {error.mean()}")
            history.append(error.mean())
        return history
            
    def predict(self, inputs):
        return self.sigmoid(np.dot(inputs, self.weights) + self.bias)
        
model = NeuralNetwork()
print("Kezdeti súly értékek:", model.weights)

train_x = np.array([
    [0,0,1],
    [1,1,1],
    [1,0,1],
    [0,1,0]
]) # 4*3-as mátrix
train_y = np.array([[0], [1], [1], [0]]) # 4*1-es mátrix
history = model.train(train_x, train_y, 100)

print("Tanítás utáni súly értékek:", model.weights)

test_x = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1],
])

print("# "*30)
print(model.predict(test_x))

plt.plot(history)
plt.show()