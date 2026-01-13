# def BubbleSort(L):
#     n = len(L)
#     if n <= 1:
#         return L
#     for i in range(n):
#         for j in range(n-i-1):
#             if L[j] < L[j+1]:
#                 L[j],L[j+1] = L[j+1],L[j]

#     return L




# PRACTICE

def BubbleSort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

    return nums

print(BubbleSort([4,5,2,1,3]))