def fibonacci(n):
    # Initialize the list with the first two terms: 0 and 1
    fib_series = [0,1]
     # Loop from the third term to the nth term
    for i in range(2,n):
        # Next term is the sum of the previous two terms
        next_terms = fib_series[i-1]+fib_series[i-2]
         # Append the next term to the list
        fib_series.append(next_terms)
     # Return the list of Fibonacci terms    
    return fib_series
    
n=int(input("Enter The Number Of terms:"))
print(fibonacci(n))