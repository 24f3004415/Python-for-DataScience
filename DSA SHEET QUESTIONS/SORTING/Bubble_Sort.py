def BubbleSort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        for j in range(n-i-1):
            if L[j] < L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]

    return L

print(BubbleSort([4,5,2,1,3]))