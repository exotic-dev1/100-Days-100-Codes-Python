"""
Day86 :- Longest Common Subsequence
Difficulty :- Medium
Concepts :- DP, strings, subsequences
"""
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example
s1 = "abcde"
s2 = "ace"

print(longest_common_subsequence(s1, s2))