def squares_of_sorted_array(nums):
  """
  Finds the squares of the elements in nums and sorts them in non-decreasing order.

  Args:
    nums: An integer array sorted in non-decreasing order.

  Returns:
    An array of the squares of the elements in nums sorted in non-decreasing order.
  """

  squared_nums = []
  for num in nums:
    squared_nums.append(num * num)
  squared_nums.sort()
  return squared_nums


if __name__ == "__main__":
  nums = [-4, -1, 0, 3, 10]
  print(squares_of_sorted_array(nums))