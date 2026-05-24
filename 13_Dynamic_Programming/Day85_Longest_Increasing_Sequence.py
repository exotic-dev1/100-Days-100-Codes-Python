"""
Day85 :- Longest Increasing Subsequence
Difficulty :- Medium
Concepts :- DP, subsequences
"""
def longest_increasing_subsequence(nums):
    n = len(nums)

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr))