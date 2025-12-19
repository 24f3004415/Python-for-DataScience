# 145 - 1^3, 4^3, 5^3
# % -> used to extract last digit


n = int(input("Enter a number : "))
i = len(str(n))
copy = n
sum = 0
while n>0:
    digits = n % 10
    sum += digits**i
    n = n//10

if sum == copy :
    print("It's a Armstrong!!")

else:
    print("Not a Armstrong!!")