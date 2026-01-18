lst = [1, 8, 7, 56, 90]
largest_num = float('-inf')
for i in lst:
    if i > largest_num:
        largest_num = i

print(largest_num)