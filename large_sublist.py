def find_largest_sublist(lst):
 max_length = 0
 start = 0
 seen = {}
 result = []
 for end, num in enumerate(lst):
  if num in seen and seen[num] >= start:
    start = seen[num] + 1
 seen[num] = end
 if end - start + 1 > max_length:
    max_length = end - start + 1
 result = lst[start:end+1]
 return result
input_list = [2, 4, 5, 2, 4, 5, 7, 8, 9, 10, 4, 8, 6]
print(find_largest_sublist(input_list)) 
