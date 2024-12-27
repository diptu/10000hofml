# -*- coding: utf-8 -*-
"""deep-ml.py
"""

# problem 2: Solution 01

# def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
#   return [list(i) for i in zip(*a)]

# print(transpose_matrix([[1,2],[3,4],[5,6]]))

# problem 2 :  Solution 02


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    rows = len(a)
    cols = len(a[0]) if rows > 0 else 0  # Handle empty matrix case

    transpose = []
    for _ in range(cols):  # Iterate over columns
        new_row = []
        for _ in range(rows):  # Iterate over rows
            new_row.append(0)
        transpose.append(new_row)

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = a[i][j]

    return transpose


print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
