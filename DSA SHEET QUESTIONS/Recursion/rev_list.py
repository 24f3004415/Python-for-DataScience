lst = [1, 2, 3, 4, 5, 6, 7]
l = 0
r = len(lst)-1

while l<r:
    lst[l],lst[r] = lst[r], lst[l]
    l += 1
    r-= 1

print(lst)