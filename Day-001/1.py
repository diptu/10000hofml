""" Systems of linear equations can be solved with arrays and NumPy.
 A system of linear equations is shown below:
          8x + 3y -2z = 9
         -4x + 7y + 5z = 15
        -3x + 4y - 12z = 35
"""

import numpy as np


def main():
    A = np.array([[8, 3, -2], [-4, 7, 5], [-3, 4, -12]])
    b = np.array([9, 15, 35])

    X = np.linalg.solve(A, b)
    x = X[0]
    y = X[1]
    z = X[2]
    print(f"x = {x}, y = {y}, z = {z}")
    test = 8 * x + 3 * y - 2 * z
    print(f" 8x + 3y -2z ={test}")


if __name__ == "__main__":
    main()
