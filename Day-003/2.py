""" Inverse of a Matrics.
 A system of linear equations is shown below:
        x + 3y = 7
        2x + 6y = 14
"""

import numpy as np
from numpy.linalg import inv


def solve(A):
    try:
        # Attempt to calculate the inverse
        inv_A = inv(A)
        print(inv_A)
    except np.linalg.LinAlgError as e:
        # Handle the error by printing a message
        print(f"Error computing inverse: {e}")
        return
    I = np.dot(A, inv_A).astype(int)
    if np.allclose(I, np.eye(A.shape[0])) == True:
        print("Matrix is invertable")


def main():
    A = np.array([[1, 3], [2, 6]])
    solve(A)


if __name__ == "__main__":
    main()
