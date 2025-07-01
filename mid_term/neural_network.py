from abc import ABC, abstractmethod
import numpy as np

class Layer(ABC):
    @abstractmethod
    def forward(self, x):
        pass
    
    @abstractmethod
    def backward(self, grad):
        pass

class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
    
    # Implement these
    def forward(self, x):
        return np.dot(x, self.weights)
    
    def backward(self, grad):
        return np.dot(grad, self.weights.T)

# Test Input
dense = Dense(3, 2)
print(dense.forward(np.array([[1,2,3]])))  # Should compute matrix product