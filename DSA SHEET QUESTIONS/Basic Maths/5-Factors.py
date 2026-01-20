# from math import sqrt

# num = 36
# factors = []
# for i in range(1,int(sqrt(num))+1):
#     if num%i == 0:
#         factors.append(i)
#         if num//i != i:
#             factors.append(num//i)

# print(factors)



num = 36  # √36 = 6
factors = []

# Loop from 1 to √num + 1
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:  # If i divides num evenly
        if i != num // i:  # If i and num//i are different
            factors.append(i)
            factors.append(num // i)
            
        else:  # If i == num//i (perfect square case)
            factors.append(i)

print(factors)  # Output: [36, 1, 18, 2, 12, 3, 9, 4, 6]