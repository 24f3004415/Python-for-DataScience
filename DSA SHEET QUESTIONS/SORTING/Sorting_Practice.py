# Merge Sort
def merge_array(nums,left,right):
    result = []
    n,m = len(left), len(right)
    i,j = 0,0

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i <= n:
        result.append(left[i])
        i += 1

    while j <= m:
        result.append(right[j])
        j += 1

    return result