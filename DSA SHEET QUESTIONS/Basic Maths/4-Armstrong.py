num = int(input("Enter a number: "))

def digitCount(n):
    count = 0
    while n>0:
        count += 1
        n = n//10
    return count

copy = num
result = 0 
count = digitCount(num)
while num>0:
    l_digit = num%10
    result = result + (l_digit**count)
    num = num//10

if copy == result:
    print("Armstrong!!")
else:
    print("Not an Armstrong..")

