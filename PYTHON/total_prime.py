n = int(input("enter a number till where you want to check prime: "))

count = 0

for i in range (1,n+1):
    if n%i == 0:
        count += 1
    if count == 2:
        print(f"{i} is a prime number")

    else:
        print(f"{i} is not a prime number")