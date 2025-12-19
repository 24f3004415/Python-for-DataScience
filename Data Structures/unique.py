lst = [1,1,1,1,2,2,2,3,3,3,4,4,4]
unique_lst = []
for i in range(len(lst)):
    if lst[i] not in unique_lst:
        unique_lst.append(lst[i])

print(unique_lst)