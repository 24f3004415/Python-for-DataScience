n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

hcf = 1
for i in range(n1, 1, -1):
    if n1 % i == 0 and n2 % i == 0:
        hcf = i
        break

print("HCF of", n1, "and", n2, "is -> ", hcf)