from SmartGrass.network import Network
from SmartGrass.activations import sigmoid, sigmoid_deriv
from SmartGrass.losses import mse, mse_deriv
from SmartGrass.activation_layer import Activation
from SmartGrass.fclayer import FCLayer
import numpy as np

model = Network()
model.add(FCLayer(5, 10))
model.add(Activation(sigmoid, sigmoid_deriv))
model.add(FCLayer(10, 1))
model.add(Activation(sigmoid, sigmoid_deriv))
model.use_loss(mse, mse_deriv)

x_train = np.array([
    [1,0,1,1,0],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [0,0,1,0,1],
    [1,1,1,0,0],
    [0,0,0,0,0]
])

print(model.predict(x_train))

