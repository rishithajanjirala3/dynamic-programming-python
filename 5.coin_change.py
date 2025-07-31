# Concept: Unbounded knapsack
# Use Case: Currency systems, payment gateways

# Coin Change - Minimum number of coins

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Sample Input
coins = [1, 2, 5]
amount = 11

# Output: 3
print(coinChange(coins, amount))
