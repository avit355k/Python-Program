def is_palindrome(word):
    return word == word[::-1]

def largest_palindrome(words):
    largest_word = ""
    for word in words:
        if is_palindrome(word) and len(word) > len(largest_word):
            largest_word = word
    return largest_word

words = []

# Taking input from the user
num_of_words = int(input("Enter the number of words: "))
for i in range(num_of_words):
    word = input("Enter word: ")
    words.append(word)
    
print("Largest palindrome:", largest_palindrome(words))
