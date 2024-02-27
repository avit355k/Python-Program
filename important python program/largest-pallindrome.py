def is_palindrome(word):
    return word == word[::-1]
palindrome=[]
words = input("Enter a list of words").split()
for word in words:
    if is_palindrome(word):
        palindrome.append(word)

largest = max(palindrome,key=len)
print("The largest pallindrome: ",largest)