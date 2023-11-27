class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        
        # 1a + 0b = 1
        # 1a + 1b = 0.5
        # 0a + 1b = -0.5
        # 0a + 0b = 0


        # _and = 1 if 11, else 0
        _and = 1 if (sum(w*i for w, i in zip(self.weights, inputs))) > 0 else 0
        # 11->1 else 0
        _or = 0 if (sum(w*i for w, i in zip(self.weights, inputs))) # 00->0
        _nand =
        _xor = 
        # Aplica a função degrau para determinar a saída
        return {
            "and": _and,
            "or": _or,
            "nand": _nand,
            "xor": _xor
        }
# Exemplo de uso
if __name__ == "__main__":
    # Pesos para: tempo, companhia do namorado/namorada, proximidade do transporte público
    weights = [1, 0.5]  # O peso do tempo é maior, indicando maior importância
    threshold = 0  # Limiar para a decisão

    # Cria o perceptron com os pesos e limiar pré-definidos
    perceptron = Perceptron(weights, threshold)

    # Testa o perceptron com diferentes entradas
    print(perceptron.predict([1, 0]))  # Bom tempo, sem companhia, longe do transporte
    print(perceptron.predict([0, 1]))  # Tempo ruim, com companhia, perto do transporte
    print(perceptron.predict([1, 1]))  # Bom tempo, com companhia, perto do transporte
    print(perceptron.predict([0, 0]))  # Bom tempo, com companhia, perto do transporte