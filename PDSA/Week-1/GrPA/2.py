def isPrime(num):
    if num < 2:
        return False
        
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
        
def Goldbach(n):
    result = []
    for i in range(2,int(n//2) + 1):
        j = n - i
        
        if isPrime(i) and isPrime(j):
            result.append((i,j))
            
    return result
n=int(input())
print(sorted(Goldbach(n)))