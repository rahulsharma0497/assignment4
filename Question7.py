def max_integers_in_matrix(m, n, ops):
  """
  Counts the number of maximum integers in the matrix after performing all the operations.

  Args:
    m: The number of rows in the matrix.
    n: The number of columns in the matrix.
    ops: An array of operations.

  Returns:
    The number of maximum integers in the matrix.
  """

  max_integer = 0
  count = 0
  for ai, bi in ops:
    for i in range(ai):
      for j in range(bi):
        if M[i][j] > max_integer:
          max_integer = M[i][j]
        M[i][j] += 1
  for i in range(m):
    for j in range(n):
      if M[i][j] == max_integer:
        count += 1
  return count


if __name__ == "__main__":
  m = 3
  n = 3
  ops = [[2, 2], [3, 3]]
  print(max_integers_in_matrix(m, n, ops))