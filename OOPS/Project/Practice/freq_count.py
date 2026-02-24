def count_freq(nums):
    hash_map = {}
    most_occuring = 0
    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1

    temp = 0
    for key, value in hash_map.items():
        if value > temp:
            temp = value
            most_occuring = key

    return most_occuring

L = [1,1,1,1,2,2,2,3,3,3]
to_remove = count_freq(L)

while 1 in L:
    L.remove(to_remove)
print(L)


