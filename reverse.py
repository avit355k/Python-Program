def reverse_list(input_list):
    start = 0
    end = len(input_list) - 1
    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1
    return input_list

user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(item) for item in user_input.split()]

reversed_list = reverse_list(user_list)
print("Reversed list:", reversed_list)
