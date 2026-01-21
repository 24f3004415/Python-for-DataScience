# 1. CLOCKWISE ARRAY ROTATION
# reverse(all)
# reverse(first k)
# reverse(rest)

def reverse(nums, left_idx, right_idx):
    while left_idx < right_idx:
        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        left_idx += 1
        right_idx -= 1

    return nums

arr = [1,2,3,4,5,6]
n = len(arr)
k = 3  #("How many times you want to rotate the array, Clockwise?")
k = k % n  
reverse(arr, 0, n-1)
reverse(arr, 0, k-1)
reverse(arr, k, n-1)

print(arr)


# 2. ANTI-CLOCKWISE ARRAY ROTATION
# reverse(first k)
# reverse(rest)
# reverse(all)

class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    
    def reverse(self, nums, l_idx, r_idx):
        while l_idx < r_idx:
            nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
            l_idx += 1
            r_idx -= 1

    def rotateArr(self, arr, k):
        n = len(arr)
        k = k % n
        
        # Step 1: reverse first k elements
        self.reverse(arr, 0, k - 1)
        
        # Step 2: reverse remaining elements
        self.reverse(arr, k, n - 1)
        
        # Step 3: reverse entire array
        self.reverse(arr, 0, n - 1)
        
        return arr

solution = Solution()
print(solution.rotateArr([1, 2, 3, 4, 5], 2))

