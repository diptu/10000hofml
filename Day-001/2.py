""" Systems of linear equations can be solved with arrays and NumPy.
 A system of linear equations is shown below:
          x + 2y +z = 2
         3x + 8y + z = 12
             4y  + z = 2
"""

import numpy as np


def solve(A, b):
    X = np.linalg.solve(A, b)
    x = X[0]
    y = X[1]
    z = X[2]
    return x, y, z


def main():
    A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
    b = np.array([2, 12, 2])

    x, y, z = solve(A, b)
    print(f"x = {x}, y = {y}, z = {z}")
    test = x + 2 * y + z
    print(f" x + 2y +z ={test}")


if __name__ == "__main__":
    main()
