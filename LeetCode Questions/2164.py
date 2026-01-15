# odd -> decreasing
# even -> increasing

nums = [4,1,2,3]

even = []
odd = []

for i in range(len(nums)):
    if i%2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

even.sort()
odd.sort(reverse = True)
e, o = 0,0
for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = even[e]
        e += 1

    else:
        nums[i] = odd[o]
        o += 1

print(nums)

    

