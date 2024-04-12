""" Inverse of a Matrics.
 A system of linear equations is shown below:
          8x + 3y -2z = 9
         -4x + 7y + 5z = 15
        -3x + 4y - 12z = 35
"""

import numpy as np
from numpy.linalg import inv


def solve(A):
    try:
        # Attempt to calculate the inverse
        inv_A = inv(A)
    except np.linalg.LinAlgError as e:
        # Handle the error by printing a message
        print(f"Error computing inverse: {e}")
        return
    I = np.dot(A, inv_A).astype(int)
    if np.allclose(I, np.eye(A.shape[0])) == True:
        print("Matrix is invertable")


def main():
    A = np.array([[8, 3, -2], [-4, 7, 5], [-3, 4, -12]])
    solve(A)


if __name__ == "__main__":
    main()
