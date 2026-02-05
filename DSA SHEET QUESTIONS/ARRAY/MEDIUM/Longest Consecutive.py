class Solution:
    def longestConsecutive(self, nums):
        hash = set(nums)
        longest_streak = 0

        for num in hash:
            if num - 1 not in hash:
                x = num
                current_streak = 1
                while x+1 in hash:
                    current_streak += 1
                    x += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

solution = Solution()
print(solution.longestConsecutive(nums = [100,4,200,1,3,2]))