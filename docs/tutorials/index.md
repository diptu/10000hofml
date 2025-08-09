# 📅 Day 01 – Linear Regression (from Scratch)

Welcome to **Day 01** of the [100 Days of ML/DL](../../index.md) challenge!  
Today’s focus is on understanding and implementing **Linear Regression from scratch** using pure Python and NumPy — no ML libraries like Scikit-learn.


## Suggested Readings:
- [Linear Regression-MLU](https://mlu-explain.github.io/linear-regression/)
- **Intro to Machine Learning:Coursera**:
    - [Week 01]((https://www.coursera.org/learn/machine-learning/home/week/1))
    - [Week 02](https://www.coursera.org/learn/machine-learning/home/week/2)
- [Linear Regression-CampusX](https://www.youtube.com/watch?v=UZPfbG0jNec&list=PLKnIA16_Rmva-wY_HBh1gTH32ocu2SoTr&index=1)
- [Comprehensive Guide to Linear Regression: Examples and Model Diagnostics](https://blog.bytescrum.com/comprehensive-guide-to-linear-regression-examples-and-model-diagnostics)
- [Where Did The Assumptions of Linear Regression Originate From?](https://www.dailydoseofds.com/where-did-the-assumptions-of-linear-regression-originate-from/)

---


## 📌 What You'll Learn

- What Linear Regression is
- How it models the relationship between input and output
- Implementing it using gradient descent
- Evaluating model performance using R² (coefficient of determination)

---

## 📈 Linear Regression Overview

Linear Regression is one of the simplest and most widely used supervised learning algorithms. It attempts to model the relationship between a scalar dependent variable `y` and an independent variable `x` by fitting a linear equation:

\[
y = wx + b
\]

!!! info "Where:"
- `w` is the **slope**
- `b` is the **intercept**

The goal is to minimize the **Mean Squared Error (MSE)** between the predicted and actual values.

---

## 📉 Squared Error Cost Function:

In Linear Regression, the **cost function** measures how well our model's predictions match the actual data. The most commonly used cost function is the **Mean Squared Error (MSE)**.
MSE quantifies how close a predicted value is to the true value, so we'll use it to quantify how close a regression line is to a set of points. MSE works by squaring the distance between each data point and the regression line, summing the squared values, and then dividing by the number of data points
$$
\text{MSE} = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}_i - y_i \right)^2
$$

---

### 🧮 Cost Function Formula

\[
J(w, b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

### 🧮 For later conviniance updated Formula
\[
J(w, b) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

!!! info "Notation"

- \( n \) is the number of training examples
- \( y_i \) is the actual output for the \( i \)-th training example
- \( \hat{y}_i = wx_i + b \) is the predicted output from the model
- \( w \) is the slope (weight)
- \( b \) is the intercept (bias)

---

### 🔍 Intuition

The cost function calculates the **average of the squared differences** between the predicted values and the actual values. Squaring ensures that:
- Errors don't cancel out
- Larger errors are penalized more than smaller ones

The goal of training is to **minimize this cost** by adjusting the parameters \( w \) and \( b \).

---

### ✅ Python Equivalent

```python
def compute_cost(X, y, w, b):
    n = len(X)
    predictions = w * X + b
    errors = y - predictions
    cost = (1/n) * np.sum(errors ** 2)
    return cost

```

### 🎯 Goal Function

To minimize the cost, we want to find the values of \( w \) and \( b \) that result in the **smallest possible value of \( J(w, b) \)**:

\[
\min_{w, b} \; J(w, b)
\]

This means:
> Find the values of **\( w \)** and **\( w \)** that make the sum of squared prediction errors as small as possible.

---

### 🔧 How Do We Minimize It?

We typically use an optimization algorithm such as **Gradient Descent**, which updates \( m \) and \( b \) iteratively in the direction of the negative gradient:

\[
\begin{aligned}
w &:= w - \alpha \cdot \frac{\partial J}{\partial w} \\
b &:= b - \alpha \cdot \frac{\partial J}{\partial b}
\end{aligned}
\]

!!! info "Notation"
- \( \alpha \) is the **learning rate**
- \( \frac{\partial J}{\partial m} \), \( \frac{\partial J}{\partial b} \) are the **partial derivatives** of the cost function

---

### 📐 Compute the Partial Derivative

Let’s expand the derivative of the cost function with respect to \( w \):

\[
\frac{\partial J}{\partial w} = \frac{\partial}{\partial w} \left[ \frac{1}{2n} \sum_{i=1}^{n} (y_i - (w x_i + b))^2 \right]
\]

Apply the chain rule:

\[
\frac{\partial J}{\partial w} = \frac{-1}{n} \sum_{i=1}^{n} x_i \cdot (y_i - (w x_i + b))
\]

---

### 🧮 Final Expanded Update Equation

\[
w := w + \alpha \cdot \frac{1}{n} \sum_{i=1}^{n} x_i \cdot (y_i - (w x_i + b))
\]

Similarly, for \( b \):

\[
b := b + \alpha \cdot \frac{1}{n} \sum_{i=1}^{n} (y_i - (w x_i + b))
\]

Where:
- \( \alpha \) is the **learning rate**
- \( x_i \), \( y_i \) are training samples
- \( w \), \( b \) are the parameters being learned

---


### 🧠 Final Objective

Find:

\[
(w^*, b^*) = \arg\min_{w, b} J(w, b)
\]

Such that predictions are as accurate as possible based on the training data.


<!-- ## 🧪 Files Included -->

### ✅ Python Implementation

```python title="LinearRegression.py" 
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

```