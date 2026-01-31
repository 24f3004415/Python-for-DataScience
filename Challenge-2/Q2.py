def minmax(nums):
    remaimimg = 0
    for i in range(len(nums)//2):
        if i % 2 == 0:
            remaimimg = min(nums[2*i], nums[2*i+1])

        else:
            remaimimg = max(nums[2*i], nums[2*i+1])

    return remaimimg

print(minmax(nums = [1,2,3,4,5,6,7,8,9,10]))
