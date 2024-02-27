#program for checking the largest number among three number!!!
a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))
c = float(input("Enter Third Number:"))

largest = 0

if a > b and a > c :
    largest = a
elif b > c :
    # as the 1st condition dont match so b is already is gretter than a,
    #so we have to check only is b is gretter than c or not!!
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.")