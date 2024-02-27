def remove_duplicates(input_list):
  unique_list = []
  for item in input_list:
    if item not in unique_list:
      unique_list.append(item)
  return unique_list
user_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
unique_list = remove_duplicates(user_list)
print("The unique list is: ", unique_list)