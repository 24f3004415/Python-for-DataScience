from math import sqrt
# num = int(input('Enter a number: '))

# if num <= 1:
#     print('Not a prime Number')
# else:
#     is_prime = True
#     for i in range(2, int(sqrt(num)) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print('Its a prime number')
#     else:
#         print('Not a prime Number')

def isPrime(n):
    if n<=1:
        return False
    
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False

    return True

#Test cases
print(isPrime(36))
print(isPrime(37))
print(isPrime(1))
print(isPrime(5))