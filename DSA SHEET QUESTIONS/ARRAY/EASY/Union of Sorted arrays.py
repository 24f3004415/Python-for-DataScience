class Solution:
    def findUnion(self, left, right):
        # code here 
        i,j = 0,0
        n,m = len(left), len(right)
        
        result = []
        
        while i < n and  j < m:
            if left[i] <= right[j]:
                if len(result) == 0 or left[i] != result[-1]:
                    result.append(left[i])
                i += 1
            
            else:
                if len(result) == 0 or right[j] != result[-1]:
                    result.append(right[j])
                j += 1
                
        while i < n:
            if len(result) == 0 or left[i] != result[-1]:
                result.append(left[i])
            i += 1
            
        while j < m:
            if len(result)== 0 or right[j] != result[-1]:
                result.append(right[j])
            j += 1
            
        return result

solution = Solution()
print(solution.findUnion(left = [1, 2, 3, 4, 5], right = [1, 2, 3, 6, 7]))