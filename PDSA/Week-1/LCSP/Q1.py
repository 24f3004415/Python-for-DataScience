def is_Prime(num):
    if num < 2:
        return False

    for i in range(2,  int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
        
def prime_product(m): #m = 12
    if m<=0:
        return False

    for i in range(1, (m//2) + 1): #i = 1,2,3,4,5,6
        if m % i ==0:
            to_check = m//i

            if is_Prime(to_check) and is_Prime(i):
                return True
    else:
        return False

n = int(input())
print(prime_product(n))