class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        return nums
    
    def reverseArray(self, arr):
        # code here
        self.reverse(arr, 0, len(arr)-1)
        
        return arr