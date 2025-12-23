# Method - 1
from math import log10

num = abs(int(input("Enter a digit: ")))

if num == 0:
    print("1")
else:
    print(int(log10(num))+1)

# Method - 2
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     count += 1
#     num = num // 10

# print(count)