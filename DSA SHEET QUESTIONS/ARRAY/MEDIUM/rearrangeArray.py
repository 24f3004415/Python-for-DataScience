class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive_array = []
        negative_array = []
        result = []
        
        for i in range(n):
            if nums[i] >= 0:
                positive_array.append(nums[i])
            else:
                negative_array.append(nums[i])

        even_counter = 0
        odd_counter = 0

        for i in range(n):
            if i % 2 == 0:
                result.append(positive_array[even_counter])
                even_counter += 1
            else:
                result.append(negative_array[odd_counter])
                odd_counter += 1

        return result