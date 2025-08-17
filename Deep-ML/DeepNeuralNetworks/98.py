"""
Module implementing the Parametric ReLU (PReLU) activation function.
"""

from typing import Union


def prelu(x: Union[float, int], alpha: float = 0.25) -> float:
    """
    Apply the PReLU (Parametric ReLU) activation function.

    Parameters
    ----------
    x : float or int
        Input value.
    alpha : float, optional, default=0.25
        Slope parameter applied when ``x`` is negative.

    Returns
    -------
    float
        Output after applying the PReLU function.
    """
    return float(x) if x > 0 else float(alpha * x)


if __name__ == "__main__":
    x_val: float = -2.0
    alpha_val: float = 0.25
    print(prelu(x_val, alpha_val))  # -0.5
