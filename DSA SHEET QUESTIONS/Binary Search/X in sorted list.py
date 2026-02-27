# Iterative Method

def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2   # avoids overflow
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

# Recursive Method

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)