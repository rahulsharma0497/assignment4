def max_pair_sum(nums):
  """
  Groups the integers in nums into n pairs to maximize the sum of the minimum elements.

  Args:
    nums: An integer array of 2n integers.

  Returns:
    The maximum sum of the minimum elements in the pairs.
  """

  nums.sort()
  sum = 0
  for i in range(0, len(nums), 2):
    sum += min(nums[i], nums[i + 1])
  return sum


if __name__ == "__main__":
  nums = [1, 4, 3, 2]
  print(max_pair_sum(nums))