# def rotate(nums: List[int], k: int):
#     n = len(nums)
#     k = k % n
        
#     # Helper function to reverse a portion of the array
#     def reverse(start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1
        
#     # Step 1: Reverse entire array
#     reverse(0, n - 1)
#     # Step 2: Reverse first k elements
#     reverse(0, k - 1)
#     # Step 3: Reverse remaining elements
#     reverse(k, n - 1)





# PRACTICE
def reverse(nums, left_idx, right_idx):
    while left_idx < right_idx:
        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        left_idx += 1
        right_idx -= 1
    return nums

nums = [1,2,3,4,5,6]
k = 3
n = len(nums)
k = k % n

reverse(nums, 0, n-1)      # Step 1: Reverse entire array → [6,5,4,3,2,1]
reverse(nums, 0, k-1)      # Step 2: Reverse first k elements → [4,5,6,3,2,1]
reverse(nums, k, n-1)      # Step 3: Reverse remaining elements → [4,5,6,1,2,3]

print(nums)  




