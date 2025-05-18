#Legyen egy absztrakt ősosztály
# Ha egy osztály absztrakt, akkor sosem példányosítjuk
# A különböző réteg típúsokat, ez alapján fogjuk definiálni

class Layer:
    def __init__(self):
        self.input = None
        self.output = None
        
    def forward_propagation(self, input):
        raise NotImplementedError
    
    def backward_propagation(self, output_error, learning_rate):
        raise NotImplementedError