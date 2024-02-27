def is_prime(n):
    """
    Function to check if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_factors(n):
    """
    Function to find the prime factors of a number
    """
    prime_factors = []
    i = 2
    while i <= n:
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
        i += 1
    return prime_factors

def find_numbers(nums):
    """
    Function to find the numbers that can be represented as the product of 3 prime numbers
    """
    for num in nums:
        prime_factors = find_prime_factors(num)
        if len(prime_factors) == 3:
            print(num)

nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]
find_numbers(nums)
