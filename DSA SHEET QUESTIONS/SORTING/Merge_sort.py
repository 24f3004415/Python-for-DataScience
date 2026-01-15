def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)

    while i<n and j<m:          #1st mistake made here
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    if i < n:       
        while i < n:
            result.append(left[i])
            i+=1

    if j < m:
        while j < m:            #2nd mistake made here
            result.append(right[j])
            j += 1

    return result 

def merge_sort(nums):
    if len(nums) <= 1:          #3rd Mistake made here
        return nums

    mid = int(len(nums)//2)
    left_arr = nums[:mid]
    right_arr = nums[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left, right)

print(merge_sort([4,5,2,1,3]))