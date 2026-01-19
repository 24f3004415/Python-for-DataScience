nums = [1,2,3,4,5,6]
n = len(nums)
k = 3

# Method-1 ---> Slicing
for i in range(k):
    nums[:] = [nums[n-1]] + nums[:n-1]

print(nums)

# Method-1 ---> Loop

for i in range(k):
    temp = nums[n-1]
    for j in range(n-2,-1,-1):
        nums[j+1] = nums[j]
    nums[0] = temp

print(nums)