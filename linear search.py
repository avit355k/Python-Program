# Linear Search in Python
def linear_search(lst, target):
  for i in range(len(lst)):
    if lst[i] == target:
      return i
  return -1
# A sorted list of numbers
lst = [2, 4, 7, 11, 15, 19, 45]

# Ask the user to enter a number to search
p = int(input("Enter a number to search: "))

# Call the linear search function with the list and the number
result = linear_search(lst, p)

# Print the result
if result == -1:
  print("Search unsuccessful")
else:
  print("Search successful")
