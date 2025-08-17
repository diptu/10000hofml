"""Hard Sigmoid activation function implementation."""

from typing import Union


def hard_sigmoid(x: Union[float, int]) -> float:
    """
    Apply the Hard Sigmoid activation function.

    The Hard Sigmoid function is a computationally cheaper approximation
    of the standard sigmoid. It clips outputs below 0 and above 1, and
    linearly scales values in between.

    Formula
    -------
    hard_sigmoid(x) =
        0.0                  if x <= -2.5
        1.0                  if x >= 2.5
        0.2 * x + 0.5        otherwise

    Parameters
    ----------
    x : float or int
        Input scalar value.

    Returns
    -------
    float
        Output after applying Hard Sigmoid.

    Examples
    --------
    >>> hard_sigmoid(-3.0)
    0.0
    >>> hard_sigmoid(3.0)
    1.0
    >>> hard_sigmoid(1.0)
    0.7
    """
    if x <= -2.5:
        return 0.0
    if x >= 2.5:
        return 1.0
    return 0.2 * float(x) + 0.5


if __name__ == "__main__":
    X_VAL = 0.56
    print(hard_sigmoid(X_VAL))  # 0.612
