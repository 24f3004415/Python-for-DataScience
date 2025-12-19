a = 0
b = 1

n = int(input("Enter the number till where you want to print the series: "))

for i in range(n+1):
    print(a)
    a,b = b,a+b