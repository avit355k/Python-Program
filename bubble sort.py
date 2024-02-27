# Define a function to perform bubble sort on a list
def bubble_sort(lst):
  # Get the length of the list
  n = len(lst)
  # Loop through the list n-1 times
  for i in range(n-1):
    # Loop through the list from 0 to n-i-1
    for j in range(0, n-i-1):
      # Compare adjacent elements and swap them if they are in wrong order
      if lst[j] < lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
  # Return the sorted list
  return lst

# Input n numbers into a list
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
  num = int(input("Enter element {}: ".format(i+1)))
  lst.append(num)

# Print the original list
print("The original list is:", lst)

# Call the bubble sort function and print the sorted list
sorted_lst = bubble_sort(lst)
print("The sorted list is:", sorted_lst)
