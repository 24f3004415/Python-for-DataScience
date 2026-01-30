def KadaneAlgorithm(nums):
    total = 0
    maxi = float('-inf')
    n = len(nums)

    for i in range(n):
        total += nums[i]

        maxi = max(total, maxi)

        if total < 0:
            total = 0

    return maxi

print(KadaneAlgorithm([2, 3, -8, 7, -1, 2, 3]))