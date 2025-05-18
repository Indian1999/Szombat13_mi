class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_deriv = None
        
    def add(self, layer):
        self.layers.append(layer)
        
    def __add__(self, layer): # + operátor működése  ( model += Layer())
        self.layer.append(layer)
        
    def use_loss(self, loss, loss_deriv):
        self.loss = loss
        self.loss_deriv = loss_deriv
        
    def predict(self, input):
        samples = len(input)
        result = []
        for i in range(samples):
            output = input[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        return result