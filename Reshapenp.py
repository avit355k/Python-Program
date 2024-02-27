import numpy as np

# Create a NumPy array with 1 to 12 elements
original_array = np.arange(1, 13)

# Display the original array
print("Original Array:")
print(original_array)

# Reshape the array to a 3x4 matrix
reshaped_array = original_array.reshape(3, 4)

# Display the reshaped array
print("\nReshaped Array (3x4):")
print(reshaped_array)

# Reshape the array to a 4x3 matrix
reshaped_array = original_array.reshape(4, 3)

# Display the reshaped array
print("\nReshaped Array (4x3):")
print(reshaped_array)

# Reshape the array to a 2x6 matrix
reshaped_array = original_array.reshape(2, 6)

# Display the reshaped array
print("\nReshaped Array (2x6):")
print(reshaped_array)
