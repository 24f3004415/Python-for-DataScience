# Factorial of a number
n = int(input("Enter a number you want to calculate factorial - "))
fact = 1
for i in range (1,n+1):
    fact = fact*i

print(fact)

# Print all the numbers which are either divisible by 3 or 5 in a range

r = int(input("Enter a number till where you want to check divisibility of 3 & 5: "))
for i in range(1,r+1):
    if i%3 == 0 and i%5 == 0:
        print(i, " is divisble by both 3 and 5")

    elif i%3 == 0:
        print(i, " is divisble by 3")

    elif i%3 == 0:
        print(i, " is divisble by 5")

    else:
        print(i," is neither divisble by 3 nor 5")


#25. Find the factors

m = int(input("Enter a number you want to calculate factor of - "))
count = 0
for i in range (1, m+1):
    if m%i == 0:
        print(f"{i} is the factor of {m}")
        count+=1

    else:
        print(f"{i} is not the factor of {m}")

if count<=2:
    print (f"congrtulation!!! {m} is also a prime number...")

else:
    print(f"{m} is not a prime number...")