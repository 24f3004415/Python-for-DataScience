def expanding(L):
    isExpanding = True
    check = float('-inf')
    i = 0
    j = 1
    while j < len(L):
        curr_diff = abs(L[i] - L[j])
        i += 1
        j += 1
        if curr_diff > check :
            check = curr_diff
        else:
            isExpanding = False
    
    if isExpanding:
        return True
    else:
        return False
        
L = eval(input())
print(expanding(L))