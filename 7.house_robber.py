# Concept: Maximum sum with non-adjacent elements
# Use Case: Security system planning, stock skipping

# House Robber - Max sum of non-adjacent houses

def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]

# Sample Input
nums = [2, 7, 9, 3, 1]

# Output: 12
print(rob(nums))
