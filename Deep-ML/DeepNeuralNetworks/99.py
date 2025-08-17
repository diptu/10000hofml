"""
Module implementing the softplus activation function.
"""

from typing import Union
import numpy as np


def softplus(x: float) -> float:
    """
    Compute the softplus activation function.

    Args:
            x: Input value

    Returns:
            The softplus value: log(1 + e^x)
    """
    # Your code here
    val = np.log(1 + np.exp(x))
    return round(val, 4)


if __name__ == "__main__":
    x_val: float = 2
    print(softplus(x_val))  # 2.1269
