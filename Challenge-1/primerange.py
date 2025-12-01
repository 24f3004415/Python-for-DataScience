n = int(input("Enter a number till where you want to print prime numbers: "))
count = 0
for i in range (1,n+1):
    for j in range (1, i+1):
        if i%j == 0:
            count += 1
    if count > 2:
        print(f"{i} is not a prime number")
    else:
        print(f"{i} is a Prime Number")
    count = 0