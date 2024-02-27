def isprime(num):
    # To check if the number is prime or not
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

n = int(input("Enter the Number you want to check: "))
isprime(n)
