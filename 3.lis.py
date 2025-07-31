# Concept: 1D DP
# Use Case: Stock price trend analysis

# Longest Increasing Subsequence

def LIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Sample Input
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# Output: 4
print(LIS(nums))
