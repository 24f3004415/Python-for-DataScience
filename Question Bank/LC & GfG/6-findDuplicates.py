class Solution:
    def findDuplicates(self, arr):
        # code here
        freq_map = {}
        result = []
        for i in arr:
            freq_map[i] = freq_map.get(i, 0) + 1
            
        for num,freq in freq_map.items():
            if freq == 2:
                result.append(num)
                
        return freq_map, result

solution = Solution()
print(solution.findDuplicates([1,2,3,4,5,6,7,8,9,5,8,9,6,5]))
