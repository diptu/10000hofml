import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionScratch:
    """
    A simple implementation of Linear Regression using Gradient Descent.

    Attributes:
        alpha (float): Learning rate.
        num_iters (int): Number of iterations for gradient descent.
        w (float): Weight parameter (slope).
        b (float): Bias parameter (intercept).
    """

    def __init__(self, alpha=0.01, num_iters=1000):
        """
        Initializes the Linear Regression model.

        Args:
            alpha (float): Learning rate. Default is 0.01.
            num_iters (int): Number of iterations. Default is 1000.
        """
        self.alpha = alpha
        self.num_iters = num_iters
        self.w = 0
        self.b = 0

    def compute_cost(self, x, y):
        """
        Computes the Mean Squared Error (MSE) cost.

        Args:
            x (ndarray): Input feature array.
            y (ndarray): Target output array.

        Returns:
            float: Computed cost.
        """
        m = x.shape[0]
        cost = 0
        for i in range(m):
            f_wb = self.w * x[i] + self.b
            cost += (f_wb - y[i]) ** 2
        return (1 / (2 * m)) * cost

    def compute_gradients(self, x, y):
        """
        Computes gradients of the cost function with respect to w and b.

        Args:
            x (ndarray): Input feature array.
            y (ndarray): Target output array.

        Returns:
            tuple: Gradients (dj_dw, dj_db)
        """
        m = x.shape[0]
        dj_dw = 0
        dj_db = 0
        for i in range(m):
            f_wb = self.w * x[i] + self.b
            error = f_wb - y[i]
            dj_dw += error * x[i]
            dj_db += error
        return dj_dw / m, dj_db / m

    def fit(self, x, y):
        """
        Trains the model using gradient descent.

        Args:
            x (ndarray): Training input features.
            y (ndarray): Training target values.
        """
        for i in range(self.num_iters):
            dj_dw, dj_db = self.compute_gradients(x, y)
            self.w -= self.alpha * dj_dw
            self.b -= self.alpha * dj_db

            if i % 100 == 0:
                cost = self.compute_cost(x, y)
                print(f"Iteration {i}: Cost={cost:.4f}, w={self.w:.4f}, b={self.b:.4f}")

    def predict(self, x):
        """
        Predicts output values using the learned model.

        Args:
            x (ndarray or float): Input feature(s).

        Returns:
            ndarray or float: Predicted value(s).
        """
        return self.w * x + self.b

    def plot(self, x, y):
        """
        Plots the training data and the learned regression line.

        Args:
            x (ndarray): Training input features.
            y (ndarray): Training target values.
        """
        plt.figure(figsize=(8, 5))
        plt.scatter(x, y, color="blue", label="Training Data")
        y_pred = self.predict(x)
        plt.plot(x, y_pred, color="red", label="Prediction")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Linear Regression Prediction")
        plt.legend()
        plt.grid(True)
        plt.show()


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    x_train = np.array([1, 2, 3, 4, 5])
    y_train = np.array([2.1, 4.0, 6.1, 8.0, 10.2])

    model = LinearRegressionScratch(alpha=0.01, num_iters=10000)
    model.fit(x_train, y_train)
    model.plot(x_train, y_train)

    # Optional: Predict new points
    x_test = np.array([6, 7])
    predictions = model.predict(x_test)
    print(f"Predictions: {predictions}")
