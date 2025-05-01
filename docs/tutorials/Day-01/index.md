# 📅 Day 01 – Linear Regression (from Scratch)

Welcome to **Day 01** of the [100 Days of ML/DL](../../index.md) challenge!  
Today’s focus is on understanding and implementing **Linear Regression from scratch** using pure Python and NumPy — no ML libraries like Scikit-learn.

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

## 📉 Squared Error Cost Function for Linear Regression

In Linear Regression, the **cost function** measures how well our model's predictions match the actual data. The most commonly used cost function is the **Mean Squared Error (MSE)**.

---

### 🧮 Cost Function Formula

\[
J(w, b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
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

Where:
- \( \alpha \) is the **learning rate**
- \( \frac{\partial J}{\partial m} \), \( \frac{\partial J}{\partial b} \) are the **partial derivatives** of the cost function

---

### 🧠 Final Objective

Find:

\[
(w^*, b^*) = \arg\min_{w, b} J(w, b)
\]

Such that predictions are as accurate as possible based on the training data.


<!-- ## 🧪 Files Included -->

