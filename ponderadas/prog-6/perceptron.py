import numpy as np

class Perceptron:
    def __init__(self, iterations = 100, threshold = 0.5, learning_rate = 0.1):
        self.iterations = iterations
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.bias = 0
        self.weights = np.zeros(2)
        print("Perceptron activated.")
        
    def activation(self, value: float) -> int:
        return 1 if value >= self.threshold else 0
            
    def predict(self, input: np.array) -> int:
        
        value = self.bias + np.dot(input, self.weights)
        predicted = self.activation(value)
        return predicted
    
    def train(self, inputs: np.array, results: np.array) :
        for _ in range(self.iterations):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                error = results[i] - prediction
                self.weights += self.learning_rate * error * inputs[i]
                self.bias += self.learning_rate * error
        print("Perceptron trained with success.")
        print(f"My bias: {self.bias}, my weight: {self.weights}")
