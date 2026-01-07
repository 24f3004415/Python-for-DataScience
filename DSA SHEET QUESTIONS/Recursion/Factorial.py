# recursion method
def fact(N):
    if N == 1:
        return 1
    return N * fact(N-1)

print(fact(5))



# same question with loop method
n = int(input("Enter a number to calculate the factorial - "))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(factorial)