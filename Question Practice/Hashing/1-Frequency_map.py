lst = [1,2,9,6,4,9,3,5,4,8,9,6,2,8,4,6,9,8,5,1,5,6,2,5,6,4,2,5,9,4,5,6,9,8,2,6,5,7,4,1,2,5,6]

freq_map = {}

for i in range(len(lst)):
    if lst[i] not in freq_map:
        freq_map[lst[i]] = 1
    else:
        freq_map[lst[i]] += 1

print(freq_map)
