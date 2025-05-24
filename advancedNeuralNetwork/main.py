from SmartGrass.network import Network
from SmartGrass.activations import sigmoid, sigmoid_deriv, tanh, tanh_deriv
from SmartGrass.losses import mse, mse_deriv
from SmartGrass.activation_layer import Activation
from SmartGrass.fclayer import FCLayer
import numpy as np

model = Network()
model.add(FCLayer(5, 10))
model.add(Activation(tanh, tanh_deriv))
model.add(FCLayer(10, 1))
model.add(Activation(tanh, tanh_deriv))
model.use_loss(mse, mse_deriv)


train_len = 30

x_train = np.random.randint(0, 2, size = (train_len, 1, 5))
y_train = []
for item in x_train:
    if item[0][0] == 1 and item[0][2] == 1:
        y_train.append(1)
    else:
        y_train.append(0)
y_train = np.array(y_train)
y_train = y_train.reshape(train_len, 1, 1)

model.fit(x_train, y_train, epochs = 100, learning_rate=0.1, reverb=True)

while True:
    bits = input("Give me 5 bits: ")
    bits = np.array(list(bits)).astype("float32")
    bits = bits.reshape(1,1,5)
    print(model.predict(bits))
