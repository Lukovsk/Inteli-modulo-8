# Atividade 6: Perceptron e portas lógicas

## Enunciado

Implementação de um perceptron capaz de ser treinado para reproduzir o comportamento das seguintes portas lógicas:

- AND
- OR
- NAND
- XOR

### Padrão de qualidade

- O sistema implementa um perceptron com: pesos, função de ativação, método de predição, método de treinamento e bias;
- O sistema treinado consegue reproduzir o comportamento das portas lógicas propostas. Quando o resultado encontrado não for o esperado, deve haver uma explicação adequada.

# Conteúdo

## Estrutura de pastas

<pre><code>prog-6/
│
├── main.py
└── perceptron.py</code> </pre>
Onde:

```main.py```: script responsável por ativar os testes da aplicação;

```perceptron.py```: script auxiliar que possui a classe do perceptron;

## Testando o perceptron

Para testar o perceptron, basta rodar o script ```main.py``` com:
<pre><code>python main.py</code></pre> 

A saída esperada é a seguinte:
<pre><code>Perceptron activated.
Perceptron trained with success.
My bias: 0.30000000000000004, my weight: [0.2 0.2]
==== For logic 'OR' gate ====
in (0, 0), out: 0
in (0, 1), out: 1
in (1, 0), out: 1
in (1, 1), out: 1

Perceptron activated.
Perceptron trained with success.
My bias: 0.5, my weight: [-0.1  0. ]
==== For logic 'XOR' gate ====
in (0, 0), out: 1
in (0, 1), out: 1
in (1, 0), out: 0
in (1, 1), out: 0

Perceptron activated.
Perceptron trained with success.
My bias: 0.7, my weight: [-0.1 -0.1]
==== For logic 'NAND' gate ====
in (0, 0), out: 1
in (0, 1), out: 1
in (1, 0), out: 1
in (1, 1), out: 0

Perceptron activated.
Perceptron trained with success.
My bias: 0.2, my weight: [0.2 0.2]
==== For logic 'AND' gate ====
in (0, 0), out: 0
in (0, 1), out: 0
in (1, 0), out: 0
in (1, 1), out: 1</code></pre>

## Explicação

Cada saída representa o perceptron sendo treinado com os dados para uma porta lógica e sua saída, além disso, também há o bias e os pesos finais nessa saída.

### XOR

Como pode ser visto, o perceptron, mesmo treinado, não acertou as relações da porta lógica *XOR*. A explicação para isso é a de que o treinamento do perceptron não o prepara para execuções não-lineares, como o XOR, que envolve uma divisão binária. 

### Demonstração

[96bbdf5c-8c16-4e72-bc0f-2e755b0cd239.webm](https://github.com/Lukovsk/Inteli-modulo-8/assets/99260684/bbf82439-00a3-48a7-a3d5-8b113223b9a8)



