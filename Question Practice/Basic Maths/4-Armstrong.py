# num = int(input("Enter a number: "))

# def digitCount(n):
#     count = 0
#     while n>0:
#         count += 1
#         n = n//10
#     return count

# copy = num
# result = 0 
# count = digitCount(num)
# while num>0:
#     l_digit = num%10
#     result = result + (l_digit**count)
#     num = num//10

# if copy == result:
#     print("Armstrong!!")
# else:
#     print("Not an Armstrong..")

def isArmstrong(num):
    if num == 0:
        return 'YES'

    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp //= 10

    result = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        result += digit ** count
        temp //= 10

    return 'YES' if result == num else 'NO'

print(isArmstrong(153))
print(isArmstrong(1634))
print(isArmstrong(568))
print(isArmstrong(1))
print(isArmstrong(0))