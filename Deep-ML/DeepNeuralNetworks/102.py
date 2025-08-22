"""
Module implementing Swish activation functions.
"""

from typing import Union
import numpy as np


def sigmoid(z: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the sigmoid activation function.

    Parameters
    ----------
    z : float or np.ndarray
        Input value or array.

    Returns
    -------
    float or np.ndarray
        Sigmoid of the input.
    """
    return 1 / (1 + np.exp(-z))


def swish(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the Swish activation function.

    Swish is defined as: x * sigmoid(x).

    Parameters
    ----------
    x : float or np.ndarray
        Input value or array.

    Returns
    -------
    float or np.ndarray
        Swish of the input.
    """
    sigma = sigmoid(x)
    return x * sigma


if __name__ == "__main__":
    x_val: float = 1.0
    print(swish(x_val))  # Expected output: 0.7311
