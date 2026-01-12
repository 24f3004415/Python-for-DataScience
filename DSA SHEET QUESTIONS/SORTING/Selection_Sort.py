def SelectionSort(L):
    n = len(L)
    if n<=1:
        return L
    
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if L[j] > L[min_idx]:
                min_idx = j
        L[i],L[min_idx] = L[min_idx],L[i]
    return L
    

print(SelectionSort([4,5,2,1,3]))