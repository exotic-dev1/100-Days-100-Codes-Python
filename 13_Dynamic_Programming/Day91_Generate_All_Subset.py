"""
Day91 :- Generate All Subsets
Difficulty :- Medium
Concepts :- backtracking, recursion
"""
def subsets(nums):
    result = []

    def backtrack(start, current):
        
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])    
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
    
nums = [1, 2, 3]
print(subsets(nums))