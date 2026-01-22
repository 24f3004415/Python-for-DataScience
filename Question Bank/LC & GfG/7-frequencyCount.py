class Solution:
    def frequencyCount(self, arr):
        #  code here
        hash_map = {}
        for i in range(len(arr)):
            hash_map[arr[i]] = hash_map.get(arr[i],0) + 1
        result = []
        for key,value in hash_map.items():
            result.append((key,value))

        return result
        

solution = Solution()
print(solution.frequencyCount([1, 1, 2, 3, 3, 3]))