lst = [1, 2, 3, 4, 5, 6, 7]

# using core logic
l = 0
r = len(lst)-1

while l<r:
    lst[l],lst[r] = lst[r], lst[l]
    l += 1
    r-= 1

print(lst)

# using reverse method
lst.reverse()
print(lst)