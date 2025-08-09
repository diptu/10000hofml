import math
import numpy as np


def softmax(scores: list[float]) -> list[float]:
    probabilities = np.exp(scores) / sum(np.exp(scores))
    return probabilities


if __name__ == "__main__":
    scores = [1, 2, 3]
    print(softmax(scores))  # [[0.0900, 0.2447, 0.6652]
