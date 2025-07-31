# Concept: Minimum operations to convert one string to another
# Use Case: Spell checker, DNA alignment

# Edit Distance (Levenshtein Distance)

def editDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],     # delete
                                   dp[i][j - 1],     # insert
                                   dp[i - 1][j - 1]) # replace

    return dp[m][n]

# Sample Input
word1 = "horse"
word2 = "ros"

# Output: 3
print(editDistance(word1, word2))
