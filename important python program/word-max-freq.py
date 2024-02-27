# Taking input from the user
file_name = input("Enter the name of the file: ")

# Reading the contents of the file
with open(file_name, "r") as file:
    contents = file.read()

# Splitting the contents into words
words = contents.split()

# Counting the frequency of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Finding the word with maximum frequency
max_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        max_count = count
        max_word = word

# Displaying the word with maximum frequency
print("The word with maximum frequency is:", max_word)
