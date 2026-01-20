nums = [0,1,0,3,12]

occurences = nums.count(0)
for _ in range(occurences):
    nums.remove(0)
    nums.append(0)

print(nums)


# OPTIMAL SOLUTION

def moveZeroes(nums: List[int]):
    left = 0  # Position to place next non-zero
        
    # Move all non-zeros to the front
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums