import math


def sigmoid(z: float) -> float:
    # Your code here
    result = round(1 / (1 + math.exp(-z)), 4)
    return result
