# There are total 3 ways to solve this question. 
# 1. Using slicing
# 2. Using List methods, And
# 3. By using reversing method.

nums = [1,2,3,4,5,6]
n = len(nums)
k = 3

# Method-1 ---> Slicing
for i in range(k):
    nums[:] = [nums[n-1]] + nums[:n-1]

print(nums)

# Method-2 ---> Loop

for i in range(k):
    temp = nums[n-1]
    for j in range(n-2,-1,-1):
        nums[j+1] = nums[j]
    nums[0] = temp

print(nums)


# Method-3 ---> List Methods


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % n
        for i in range(rotations):
            popped = nums.pop()
            nums.insert(0,popped)