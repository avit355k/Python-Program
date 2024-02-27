def higest_gcd(x, y):
  # initialize gcd to 1
  gcd = 1
  # loop from 1 to the smaller of x and y
  for i in range (1, min (x, y) + 1):
    # if i divides both x and y
    if x % i == 0 and y % i == 0:
      # update gcd to i
      gcd = i
  # return gcd
  return gcd
x=int(input("Enter The First Number:"))
y=int(input("Enter The Second Number:"))

print(higest_gcd(x,y))
