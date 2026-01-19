def removeDuplicates(nums):
    dict = {}
    count = 0
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = dict.get(nums[i], 0)

    j = 0

    for k in dict.keys():
        nums[j] = k
        j += 1
        count += 1

    return nums,count

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



