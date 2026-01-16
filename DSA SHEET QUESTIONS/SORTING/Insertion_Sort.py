# def Insertion_Sort(nums):
#     n = len(nums)
#     if n <=1 :
#         return nums

#     for i in range(1,n):
#         key = nums[i]
#         j = i-1

#         while j>=0 and nums[j] > key:
#             nums[j+1] = nums[j]
#             j -= 1

#         nums[j+1] = key

#     return nums 

# print(Insertion_Sort([4,5,2,1,3]))




def Insertion_Sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    return nums

print(Insertion_Sort([4,5,2,1,3]))