lst =  [4,8,5,6,7,4,2,3,9,1,9,8]
result = []
largest_num = float('-inf')
second_largest_num = float('-inf')
smallest_num = float('inf')
second_smallest_num = float('inf')

for i in lst:
    if i > largest_num:
        second_largest_num = largest_num
        largest_num = i
    elif i > second_largest_num and i < largest_num:
        second_largest_num = i 

    if i < smallest_num:
        second_smallest_num = smallest_num
        smallest_num = i

    elif i > smallest_num and i < second_smallest_num:
        second_smallest_num = i
        
result.append(second_largest_num)
result.append(second_smallest_num)
print(result)
