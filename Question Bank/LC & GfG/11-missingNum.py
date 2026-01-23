def findMissingNumbers(lst, start, end):
    present = set(lst)
    
    missing = []
    for num in range(start, end + 1):
        if num not in present:
            missing.append(num)
    
    return missing


lst = [1, 2, 4, 6]
result = findMissingNumbers(lst, 1, 6)
print(result)