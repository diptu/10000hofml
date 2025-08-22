"""
Module implementing the SELU (Scaled Exponential Linear Unit) activation.
"""

from typing import Union
import numpy as np


def selu(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Compute the SELU (Scaled Exponential Linear Unit) activation function.

    SELU is defined as:
    scale * x                         if x > 0
    scale * alpha * (exp(x) - 1)      if x <= 0

    Parameters
    ----------
    x : float or np.ndarray
        Input value or array.

    Returns
    -------
    float or np.ndarray
        SELU activation of the input.
    """
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    return np.where(x > 0, scale * x, scale * alpha * (np.exp(x) - 1))


if __name__ == "__main__":
    x_val: float = -1.0
    print(selu(x_val))  # Expected output: -1.111
