# -*- coding: utf-8 -*-
"""Matrix times Vector"""


def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
  if len(a[0])!= len(b):
      return -1
  res = []
  for row in a:
    value = 0
    for i in range(len(row)):
      value += row[i]*b[i]
    res.append(value)
  return res

print(matrix_dot_vector([[1,2],[2,4],[6,8],[12,4]],[1,2,3]))