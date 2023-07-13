def staircase_rows(n):
  """
  Builds a staircase with n coins.

  Args:
    n: The number of coins.

  Returns:
    The number of complete rows of the staircase.
  """

  rows = 0
  coin = 1
  while coin <= n:
    rows += 1
    n -= coin
    coin += 1
  return rows


if __name__ == "__main__":
  n = 12
  print(staircase_rows(n))