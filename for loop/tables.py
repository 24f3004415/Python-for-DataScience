t = int(input("Enter the table you want to print: "))
n = int(input("Enter the number of times you want to print: "))


# Print table
for i in range(1,11):
    print(f"{t} * {i} = {t*i}")

print([f"{t} * {i} = {t*i}" for i in range(1,11)])


# Print numbers from 1 to 10
print([i for i in range(1,n+1)])

# Print odd numbers from 1 to 20
print([i for i in range(1,21) if i%2 != 0])

# Take a number N and print the sum of numbers from 1 to N 
print(sum([i for i in range(1,n+1)]))

# OR

sum = 0
for i in range (1, n+1):
    sum += i
print(sum)
