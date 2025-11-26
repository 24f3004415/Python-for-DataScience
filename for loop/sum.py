sum_of_even = 0
sum_if_odd = 0

n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2 == 0:
        sum_of_even += i
    else:
        sum_if_odd += i
print("Sum of even numbers: ",sum_of_even)
print("Sum of odd numbers: ",sum_if_odd)