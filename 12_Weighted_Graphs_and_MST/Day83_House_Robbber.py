"""
Day83 :- House Robber
Difficulty :- Medium
Concepts :- DP, optimization
"""
def rob(nums):
    
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    n = len(nums)

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    print("DP Array:", dp)

    return dp[-1]

houses = [2, 7, 9, 3, 1]

result = rob(houses)

print("Maximum money robbed:", result)