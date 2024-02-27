import random

# Generate 100 random numbers between 101 and 200
random_numbers = [random.randint(101, 200) for _ in range(100)]

# Initialize counters for each range
range_counts = {
    '101-125': 0,
    '126-150': 0,
    '151-175': 0,
    '176-200': 0
}

# Count the frequency of numbers in different ranges
for num in random_numbers:
    if 101 <= num <= 125:
        range_counts['101-125'] += 1
    elif 126 <= num <= 150:
        range_counts['126-150'] += 1
    elif 151 <= num <= 175:
        range_counts['151-175'] += 1
    elif 176 <= num <= 200:
        range_counts['176-200'] += 1

# Print the frequency counts
for key, value in range_counts.items():
    print(f'{key}: {value}')

