# Concept: Subset sum using 1D DP
# Use Case: Fair resource division

# Partition Equal Subset Sum

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]

# Sample Input
nums = [1, 5, 11, 5]

# Output: True
print(canPartition(nums))
