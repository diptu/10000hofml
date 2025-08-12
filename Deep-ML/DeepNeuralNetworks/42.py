"""ReLU (Rectified Linear Unit) activation function implementation."""

from typing import Union


def relu(z: Union[float, int]) -> float:
    """
    Apply the Rectified Linear Unit (ReLU) activation function.

    The ReLU function returns the input value if it is greater than zero;
    otherwise, it returns zero. It is commonly used in neural networks
    to introduce non-linearity while avoiding vanishing gradient issues.

    Formula
    -------
    relu(z) = max(0, z)

    Parameters
    ----------
    z : float or int
        Input scalar value.

    Returns
    -------
    float
        Output after applying ReLU activation.

    Examples
    --------
    >>> relu(3.5)
    3.5
    >>> relu(-2.0)
    0.0
    """
    return float(z) if z > 0 else 0.0


if __name__ == "__main__":
    Z_VAL = -1
    print(relu(Z_VAL))  # 0.0
