def is_palindrome(num):
    # Initialize a variable to store the reversed number
    reversed = 0
    # Make a copy of the original number
    temp = num
    # Loop until the number becomes zero
    while num > 0:
        # Get the last digit of the number
        remainder =num % 10 
        # Add the digit to the reversed number
        reversed = reversed*10+remainder
        # Remove the last digit of the number
        num = num //10
    #check the cpoied temp original no is same with reversed numberor not!!
    if temp == reversed :
       print(temp,"is palindrome number")
    else:
       print(temp,"is not palindrome number")

num = int(input("Enter a Number:"))
is_palindrome(num)
