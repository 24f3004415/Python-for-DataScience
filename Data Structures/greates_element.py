lst = [200,96,69,77,145,20]
max = float('-inf')
s_max = float('-inf')

for i in range (len(lst)):
    if lst[i]>max:
        s_max = max
        smax_idx = i
        max = lst[i]
        max_idx = i
    elif max>lst[i]>s_max:
        s_max = lst[i]
        smax_idx = i


print(f"Max value of list is {max} at index {max_idx} and second max value is {s_max} at index {smax_idx}")