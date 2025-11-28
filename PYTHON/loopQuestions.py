# Factorial of a number
n = int(input("Enter a number you want to calculate factorial - "))
fact = 1
for i in range (1,n+1):
    fact = fact*i

print(fact)

