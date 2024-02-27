
#This program has three functions:

 #generate_string() generates a random alphanumeric string with 6 characters, including two uppercase letters, one lowercase letter, and one digit.
# count_consecutive_digits(string) takes in a string and counts the number of strings with two consecutive digits.
# generate_and_count_strings(n) generates n random strings, check if the string has two uppercase, one lowercase and one digit, if it does then it counts the number of strings with two consecutive digits.
 #You can test the program by changing the value of n to any other number you want to generate the random strings.

 #Please note that generate_string() function doesn't guarantee the specific number of uppercase, lowercase and digits in the string.
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

def count_consecutive_digits(string):
    """
    Function to count the number of strings with two consecutive digits
    """
    count = len(re.findall(r'\d{2}', string))
    return count

def generate_and_count_strings(n):
    """
    Function to generate n random strings and count the number of strings with two consecutive digits
    """
    count = 0
    for i in range(n):
        string = generate_string()
        print(string)
        if re.search(r'[A-Z]{2}',string) and re.search(r'[a-z]',string) and re.search(r'\d',string):
            count += count_consecutive_digits(string)
    return count

print(generate_and_count_strings(50))
