"""Leaky ReLU (Rectified Linear Unit) activation function implementation."""

from typing import Union


def leaky_relu(z: Union[float, int], alpha: float = 0.01) -> float:
    """
    Apply the Leaky Rectified Linear Unit (Leaky ReLU) activation.

    Unlike standard ReLU, Leaky ReLU allows a small, non-zero gradient
    when the input is negative. This helps mitigate the "dying ReLU"
    problem where neurons can become inactive.

    Formula
    -------
    leaky_relu(z) = z            if z >= 0
                    alpha * z    if z < 0

    Parameters
    ----------
    z : float or int
        Input scalar value.
    alpha : float, default=0.01
        Slope for negative inputs.

    Returns
    -------
    float
        Output after applying Leaky ReLU.

    Examples
    --------
    >>> leaky_relu(3.5)
    3.5
    >>> leaky_relu(-2.0)
    -0.02
    """
    return float(z) if z >= 0 else alpha * float(z)


if __name__ == "__main__":
    Z_VAL = -1
    print(leaky_relu(Z_VAL))  # -0.01
