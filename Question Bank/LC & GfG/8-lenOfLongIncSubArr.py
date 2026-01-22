# 8. Find the longest increasing consecutive sublist ----

# Input:
# [1, 2, 3, 1, 2, 3, 4, 1]

# Output:
# [1, 2, 3, 4]

arr = [1, 2, 3, 1, 2, 3, 4, 1]

best_start = 0
best_len = 1

curr_start = 0
curr_len = 1

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        curr_len += 1
    else:
        curr_start = i
        curr_len = 1

    if curr_len > best_len:
        best_len = curr_len
        best_start = curr_start

print(arr[best_start : best_start + best_len])


