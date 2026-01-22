class Solution:
    
    def isPerfect(self, arr):
        n = len(arr)
        i = 0
        j = n-1
        
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
            
        return True


solution = Solution()
print(solution.isPerfect([4, 6, 7, 8, 8, 7, 6, 4]))