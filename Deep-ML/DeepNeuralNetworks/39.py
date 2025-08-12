"""Log-softmax implementation with numerical stability."""

from typing import List
import numpy as np


def log_softmax(scores: List[float]) -> List[float]:
    """
    Compute the log-softmax of a vector in a numerically stable way.

    This function subtracts the maximum value from the input vector to
    avoid overflow during exponentiation. It is commonly used in machine
    learning for stable probability computation, especially in
    conjunction with cross-entropy loss.

    Formula
    -------
    log_softmax(x_i) = x_i - max(x) -
                       log(sum_j exp(x_j - max(x)))

    Parameters
    ----------
    x : list of float
        Input vector of real numbers.

    Returns
    -------
    list of float
        Log-softmax values for each element in `x`.

    Examples
    --------
    >>> log_softmax([1.0, 2.0, 3.0])
    [-2.4076, -1.4076, -0.4076]
    """
    x_arr = np.asarray(scores, dtype=float)
    max_x = np.max(x_arr)
    shifted_x = x_arr - max_x
    log_sum_exp = np.log(np.sum(np.exp(shifted_x)))
    return np.round(shifted_x - log_sum_exp, 4).tolist()


if __name__ == "__main__":
    vec = [1.0, 2.0, 3.0]
    print(log_softmax(vec))  # [-2.4076, -1.4076, -0.4076]
