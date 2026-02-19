def odd_one(nums):
    inte = 0
    flo = 0
    stree = 0
    buul = 0
    
    for i in nums:
        if type(i) == int:
            inte += 1
        if type(i) == float:
            flo += 1
        if type(i) == str:
            stree += 1
        if type(i) == bool:
            buul += 1
            
    if inte == 1:
        return 'int'
    if flo == 1:
        return 'float'
    if stree == 1:
        return 'str'
    if buul == 1:
        return 'bool'
    
print(odd_one(eval(input().strip())))