def common_elements(arr1, arr2, arr3):
  """
  Finds the integers that appeared in all three sorted arrays.

  Args:
    arr1: The first sorted array.
    arr2: The second sorted array.
    arr3: The third sorted array.

  Returns:
    A sorted array of the integers that appeared in all three arrays.
  """

  i = j = k = 0
  result = []
  while i < len(arr1) and j < len(arr2) and k < len(arr3):
    if arr1[i] == arr2[j] == arr3[k]:
      result.append(arr1[i])
      i += 1
      j += 1
      k += 1
    elif arr1[i] < arr2[j]:
      i += 1
    elif arr2[j] < arr3[k]:
      j += 1
    else:
      k += 1
  return result


if __name__ == "__main__":
  arr1 = [1, 2, 3, 4, 5]
  arr2 = [1, 2, 5, 7, 9]
  arr3 = [1, 3, 4, 5, 8]
  print(common_elements(arr1, arr2, arr3))
