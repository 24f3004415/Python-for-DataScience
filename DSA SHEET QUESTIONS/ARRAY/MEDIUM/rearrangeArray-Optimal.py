nums = [3,1,-2,-5,2,-4]

def rearrangeArray(nums):
    even = 0
    odd = 1
    i = 0
    n = len(nums)
    result = [0]*n

    while i < n:
        if nums[i] >= 0:
            result[even] = nums[i]
            even += 2
            i += 1 

        else:
            result[odd] = nums[i]
            odd += 2
            i += 1

    return result

print(rearrangeArray(nums = [3,1,-2,-5,2,-4]))
