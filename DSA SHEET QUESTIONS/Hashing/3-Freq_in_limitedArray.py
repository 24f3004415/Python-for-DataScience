
def frequencyCount(arr):
        #  code here
        hash_map = {}
        for i in range(len(arr)):
            hash_map[arr[i]] = hash_map.get(arr[i],0) + 1
        
        output = [] 
        for i in range(1,len(arr)+1):
            if i in hash_map:
                output.append(hash_map[i])
            
            else:
                output.append(0)
                
        return output

print(frequencyCount([2, 3, 2, 3, 5]))
print(frequencyCount([3, 3, 3, 3]))
print(frequencyCount([1]))