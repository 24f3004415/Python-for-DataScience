from math import sqrt
num = int(input('Enter a number: '))

if num <= 1:
    print('Not a prime Number')
else:
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print('Its a prime number')
    else:
        print('Not a prime Number')