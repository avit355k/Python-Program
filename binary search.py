# Binary Search in Python
def binary_search(lst, target):
  start = 0
  end = len(lst) - 1
  while start <= end:
    mid = (start + end) // 2
    if lst[mid] > target:
      end = mid - 1
    elif lst[mid] < target:
      start = mid + 1
    else:
      return mid
  return -1

# A sorted list of numbers (descending order)
lst = [45, 19, 15, 11, 7, 4, 2]

# Accept another number (P) to search the sorted list
p = int(input("Enter a number to search: "))

# Call the binary search function with the list and the number
result = binary_search(lst, p)

# Print the result
if result == -1:
  print("Search unsuccessful")
else:
  print("Search successful")
