n = [5, 3, 2, 2, 1, 5, 5, 1, 5, 10]
m = [10, 11, 1, 9, 5, 6, 2]


hash_map = {}
for i in range(len(n)):
    hash_map[n[i]] = hash_map.get(n[i],0) + 1

print(hash_map)

for num in m:
    if num>10 or num<1:
        print(0)
        continue
    
    if num in hash_map:
        print(hash_map[num])
    else:
        print(0)
