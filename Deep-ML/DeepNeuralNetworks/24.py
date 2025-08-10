"""Single-neuron (logistic) model utilities."""

from typing import List, Tuple
import numpy as np


def single_neuron_model(
    features: List[List[float]],
    labels: List[int],
    weights: List[float],
    bias: float,
) -> Tuple[List[float], float]:
    """
    Compute sigmoid probabilities and MSE for a single-neuron model.

    The model applies a linear transformation followed by a sigmoid:
    ``z = X @ w + b``, ``p = 1 / (1 + exp(-z))``. Outputs are rounded to
    4 decimals for readability.

    Parameters
    ----------
    features : list of list of float
        Shape ``(n_samples, n_features)``. Input feature matrix.
    labels : list of int
        Shape ``(n_samples,)``. Binary targets (0 or 1).
    weights : list of float
        Shape ``(n_features,)``. Model weights.
    bias : float
        Scalar bias term.

    Returns
    -------
    probs : list of float
        Predicted probabilities, rounded to 4 decimals.
    mse : float
        Mean squared error between predictions and labels, rounded to
        4 decimals.

    Examples
    --------
    >>> features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
    >>> labels = [0, 1, 0]
    >>> weights = [0.7, -0.4]
    >>> bias = -0.1
    >>> probs, mse = single_neuron_model(features, labels, weights, bias)
    >>> probs
    [0.4626, 0.4134, 0.6682]
    >>> mse
    0.3349
    """
    x_mat = np.asarray(features, dtype=float)  # (n_samples, n_features)
    w_vec = np.asarray(weights, dtype=float)  # (n_features,)
    y_vec = np.asarray(labels, dtype=float)  # (n_samples,)

    z_vec = x_mat @ w_vec + float(bias)  # (n_samples,)
    probs_arr = 1.0 / (1.0 + np.exp(-z_vec))  # sigmoid
    probs_arr = np.round(probs_arr, 4)

    mse = float(np.round(np.mean((probs_arr - y_vec) ** 2), 4))
    return probs_arr.tolist(), mse


if __name__ == "__main__":
    FEATURES = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
    LABELS = [0, 1, 0]
    WEIGHTS = [0.7, -0.4]
    BIAS = -0.1
    result = single_neuron_model(FEATURES, LABELS, WEIGHTS, BIAS)
    print(result)  # ([0.4626, 0.4134, 0.6682], 0.3349)
