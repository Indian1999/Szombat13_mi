from keras.datasets import mnist
import matplotlib.pyplot as plt
from SmartGrass.network import Network
from SmartGrass.activations import sigmoid, sigmoid_deriv, tanh, tanh_deriv, relu, relu_deriv
from SmartGrass.losses import mse, mse_deriv
from SmartGrass.activation_layer import Activation
from SmartGrass.fclayer import FCLayer
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
#plt.imshow(x_train[5])
#plt.show()

model = Network()
model.add(FCLayer(28*28, 256))
model.add(Activation(relu, relu_deriv))
model.add(FCLayer(256, 10))
model.add(Activation(tanh, tanh_deriv))
model.use_loss(mse, mse_deriv)


x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1]*x_train.shape[2])

x_train = x_train[:100].astype("float32") / 255
y_train = y_train[:100]
y_train = to_categorical(y_train)
model.fit(x_train, y_train, epochs=10, learning_rate=1)

print(model.predict(x_train[0]))
print(y_train[0])


