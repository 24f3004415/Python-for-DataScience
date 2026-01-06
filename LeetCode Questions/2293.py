nums = [2,9,8,5,6,2,4,4,7,8,5,6,8,7]

while len(nums)>1:
    NewNums = []
    for i in range(len(nums)//2):
        if i%2 == 0:
            NewNums.append(min(nums[2*i], nums[2*i+1]))
        else:
            NewNums.append(max(nums[2*i], nums[2*i+1]))
    nums = NewNums
print(nums) 