def isSorted(arr):
    n = len(arr)
    result = True
    for i in range(n-1):
        if arr[i+1] >= arr[i]:
            pass
        else:
            result = False
                    
        if result == False:
            return False
                    
    if result:
        return True

print(isSorted([10, 20, 30, 40, 50]))
print(isSorted([90, 80, 100, 70, 40, 30]))
print(isSorted([1, 2, 3, 5, 5, 7, 7, 7, 8, 12, 13, 15, 15, 15, 19]))  #EDGE CASE