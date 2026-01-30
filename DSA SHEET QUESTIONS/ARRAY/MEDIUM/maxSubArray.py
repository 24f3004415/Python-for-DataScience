# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(nums):
    
    maximum_sum = float('-inf')

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            maximum_sum = max(maximum_sum, sum)

    return maximum_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
