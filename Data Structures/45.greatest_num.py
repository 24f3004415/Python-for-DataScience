lst = [2000,2,96,69,699,77,145,20,1000,1,10000]
min = lst[0]

for i in range (1 , len(lst)):
    if lst[i]<min:
        min = lst[i]
        index = i

print(f"The minimum value in the list is {min} on index {index}")
