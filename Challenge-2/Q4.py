def secondLargest(nums):
    largest = float('-inf')
    s_largest = float('-inf')

    for i in range(len(nums)):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]

        if nums[i] > s_largest and nums[i] < largest:
            s_largest = nums[i]

    return s_largest

print(secondLargest(nums = [-10,-8,-6,-2,-5,-2,-6,-8,-10]))

        
