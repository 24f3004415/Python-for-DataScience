def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

def uniquePrime(nums):
    unique_prime = set()
    for num in nums:
        if isPrime(num):
            unique_prime.add(num)

    return len(unique_prime)

def primeFactors(num):
    prime_factors = []
    
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            if i != num // i:
                prime_factors.append(num//i)
                prime_factors.append(i)
            else:
                prime_factors.append(i)
    return prime_factors

def distinctPrimeFactors(nums):
    product = 1
    for num in nums:
        product *= num
    list_of_all_prime = primeFactors(product)
    unique_Prime_set = uniquePrime(list_of_all_prime)
    return unique_Prime_set

nums = [2,4,3,7,10,6]
print(distinctPrimeFactors(nums))