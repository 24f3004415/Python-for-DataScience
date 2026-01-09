# Normal loop method

# a = 0
# b = 1
# n = int(input("Enter a range till where you to print fibonacci series-- "))

# for i in range(n):
#     print(a, end=' ')
#     a,b = b,a+b


# Recursion Method

def Recursion(n):
    if n == 0 or n == 1:
        return n

    return Recursion(n-1) + Recursion(n-2)

print(Recursion(5))
    