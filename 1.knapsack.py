# Concept: DP table, binary choice (take or skip)
# Use Case: Optimization under constraint

# 0/1 Knapsack Problem - Dynamic Programming Approach

def knapsack(wt, val, W, n):
    # dp[i][w] stores the maximum value with first i items and capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Sample Input
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)

# Output: 9
print(knapsack(wt, val, W, n))
