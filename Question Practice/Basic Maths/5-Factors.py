from math import sqrt

num = int(input('Enter a number: '))
factors = []
for i in range(1,int(sqrt(num))+1):
    if num%i == 0:
        factors.append(i)
        if num//i != i:
            factors.append(num//i)

print(factors)