def find_consecutive_digits(numbers,digit1,digit2):
    result=[]
    for num in numbers:
        num = str(num)
        for i in range(len(num)-1):
            if(num[i]==str(digit1) and num[i+1]==str(digit2)):
                result.append(num)
                break
    return result
series = input("Enetr the numbers").split()
digit1 = int(input("Enter the first digit:"))
digit2 = int(input("ENter the second digit:"))
print(find_consecutive_digits(series,digit1,digit2))
