"""Hard Sigmoid activation function implementation."""

from typing import Union
import numpy as np


def elu(x: float, alpha: float = 1.0) -> float:
    """
    Compute the ELU activation function.

    Args:
            x (float): Input value
            alpha (float): ELU parameter for negative values (default: 1.0)

    Returns:
            float: ELU activation value
    """

    return round(float(x), 4) if x > 0 else round(alpha * (np.exp(x) - 1), 4)


if __name__ == "__main__":
    X_VAL = -1
    alpha = 2.0
    print(elu(X_VAL, alpha))  # -1.2642
