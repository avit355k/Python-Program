import random
import re

def generate_string():
    """
    Function to generate a random alphanumeric string with 6 characters
    """
    uppercase_letters = [chr(i) for i in range(65, 91)]
    lowercase_letters = [chr(i) for i in range(97, 123)]
    digits = [str(i) for i in range(10)]
    char_list = uppercase_letters + lowercase_letters + digits
    random.shuffle(char_list)
    string = "".join(char_list[:6])
    return string

def count_vowels(string):
    """
    Function to count the number of vowels in the string
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

def generate_and_count_strings(n):
    """
    Function to generate n random strings and count the number of strings with two vowels
    """
    count = 0
    for i in range(n):
        string = generate_string()
        print(string)
        if re.search(r'[A-Z]',string) and re.search(r'[a-z]{2}',string) and re.search(r'\d{2}',string):
            if count_vowels(string) >= 2:
                count +=1
    return count

print(generate_and_count_strings(5))
