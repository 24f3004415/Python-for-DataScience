lst = [200,96,69,77,145,20,1,2]
min = float('inf')
s_min = float('inf')

for i in range (len(lst)):
    if lst[i]<min:
        s_min = min
        smin_idx = i
        min = lst[i]
        min_idx = i
    elif min<lst[i]<s_min:
        s_min = lst[i]
        smin_idx = i


print(f"Min value of list is {min} at index {min_idx} and second min value is {s_min} at index {smin_idx}")