def factorial(n):
    if n == 0 or n == 1:
        return 1
 # Recursive case: if n is greater than 1, return n times the factorial of n-1
    else:
        return n*factorial(n-1)
# take input from user
n = int(input("Enter The Number:"))
print(factorial(n))
    
