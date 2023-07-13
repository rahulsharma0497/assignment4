def transpose(matrix):
  """
  Finds the transpose of the 2D integer array matrix.

  Args:
    matrix: A 2D integer array.

  Returns:
    The transpose of the matrix.
  """

  transposed_matrix = []
  for i in range(len(matrix[0])):
    transposed_row = []
    for j in range(len(matrix)):
      transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
  return transposed_matrix


if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(transpose(matrix))