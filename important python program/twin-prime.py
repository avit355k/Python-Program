def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def twin_primes(m,n):
    twin_primes_list=[]
    for i in range(m,n+1):
        if is_prime(i) and is_prime(i+2):
            twin_primes_list.append((i,i+2))
    return twin_primes_list

m = int(input("Enter start"))
n = int(input("Enter ending number:"))

print(twin_primes(m,n))