lst = [2000,2,96,69,699,77,145,20,1000,10000]
max = 0

for i in range(len(lst)):
    if lst[i]>max:
        max = lst[i]
        index = i

print(f"The maximum value in the list is {max} on index {index}")