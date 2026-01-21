def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def countPrimes(n):
    count = 0
    for i in range(1, n):
        Prime = isPrime(i)
        if Prime:
            count += 1

    return count

print(countPrimes(10))