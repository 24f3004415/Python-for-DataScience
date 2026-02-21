# Source - https://stackoverflow.com/q/64600112
# Posted by pyring, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-21, License - CC BY-SA 4.0


# Rough Work
# d = {1: 'S2', 2: 'S1', 3: 'S1', 4: 'S5', 5: 'S3', 6: 'S5', 7: 'S3', 8: 'S1', 9: 'S10', 10: 'S7'}

# sorted_d = dict(sorted(d.items(), key = lambda item: item[1]))
# print(sorted_d)

# for key, value in sorted_d.items():
#     print(key, value)

def histogram(nums):
    result = []
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
        
    sorted_hash_map_by_keys = dict(sorted(hash_map.items()))
    
    sorted_hash_map_by_values = dict(sorted(sorted_hash_map_by_keys.items(), key = lambda item: item[1]))
    
    
    for key,value in sorted_hash_map_by_values.items():
        result.append((key,value))
        
    return result

L=eval(input())
print(histogram(L))