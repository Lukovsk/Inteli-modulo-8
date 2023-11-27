class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        total = sum(w * i for w, i in zip(self.weights, inputs))
        # Aplica a função degrau para determinar a saída
        return 1 if total > self.threshold else 0

# Exemplo de uso
if __name__ == "__main__":
    # Pesos para: tempo, companhia do namorado/namorada, proximidade do transporte público
    weights = [6, 2, 2]  # O peso do tempo é maior, indicando maior importância
    threshold = 5  # Limiar para a decisão

    # Cria o perceptron com os pesos e limiar pré-definidos
    perceptron = Perceptron(weights, threshold)

    # Testa o perceptron com diferentes entradas
    print(perceptron.predict([1, 0, 0]))  # Bom tempo, sem companhia, longe do transporte
    print(perceptron.predict([0, 1, 1]))  # Tempo ruim, com companhia, perto do transporte
    print(perceptron.predict([1, 1, 1]))  # Bom tempo, com companhia, perto do transporte