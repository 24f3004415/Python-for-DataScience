num1 = 2
num2 = 3
count = 0

while num1 != 0 and num2 != 0:
    if num1 >= num2:
        num1 -= num2
        count += 1
    else:
        num2 -= num1
        count += 1

print(count)