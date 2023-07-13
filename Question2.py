def find_distinct_integers(nums1, nums2):
  """
  Finds the two lists of distinct integers that are not present in each other.

  Args:
    nums1: The first array.
    nums2: The second array.

  Returns:
    A list of two lists, where the first list contains the distinct integers in
    nums1 that are not present in nums2, and the second list contains the distinct
    integers in nums2 that are not present in nums1.
  """

  answer = [[], []]
  seen = set()
  for num in nums1:
    if num not in seen:
      answer[0].append(num)
      seen.add(num)
  seen = set()
  for num in nums2:
    if num not in seen:
      answer[1].append(num)
      seen.add(num)
  return answer


if __name__ == "__main__":
  nums1 = [1, 2, 3]
  nums2 = [2, 4, 6]
  print(find_distinct_integers(nums1, nums2))