from perceptron import Perceptron
import numpy as np


def main():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])    
    y_data = [
        {
            "name": "OR",
            "value": np.array([0, 1, 1, 1])
        },
        {
            "name": "XOR",
            "value": np.array([0, 1, 1, 0])
        },
        {
            "name": "NAND",
            "value": np.array([1, 1, 1, 0])
        },
        {
            "name": "AND",
            "value": np.array([0, 0, 0, 1])
        }
    ]

    for y in y_data:        
        perceptron = Perceptron()
        perceptron.train(X, y["value"])
        
        print(f"==== For logic '{y['name']}' gate ====")
        print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
        print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
        print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
        print(f"in (1, 1), out: {perceptron.predict([1, 1])}")
        print("")

if __name__ == "__main__":
    main()

# OR
# XOR
# NAND
# AND

"""
x    y   OR    AND     NAND    XOR
0    0   0      0        1      0
0    1   1      0        1      1
1    0   1      0        1      1
1    1   1      1        0      0
"""