# hills and valleys
nums = [2,4,1,1,6,5]
l = [nums[0]]

# creating a new list without equal adjacent neighbours
for i in range(1,len(nums)):
    if nums[i] != nums[i-1]:
        l.append(nums[i])

count = 0
for i in range(1,len(l)-1):
    if l[i+1]<l[i]>l[i-1]:
        count += 1
    elif l[i+1]>l[i]<l[i-1]:
        count += 1

print(count)

