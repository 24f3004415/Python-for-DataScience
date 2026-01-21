def getSecondLargest(arr):
    # Code Here
    largest = float('-inf')
    s_largest = float('-inf')
    for i in arr:
        if i > largest:
            s_largest = largest
            largest = i
        elif i > s_largest and i < largest:
            s_largest = i
        
    if s_largest == float('-inf'):
        return -1

    return s_largest


print(getSecondLargest([10, 10, 10]))