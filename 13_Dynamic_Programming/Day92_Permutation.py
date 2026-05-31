"""
Day92 :- Permutations
Difficulty :- Medium
Concepts :- backtracking, recursion
"""
def permutations(nums):
    result = []

    def backtrack(path, used):
        
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            
            path.append(nums[i])
            used[i] = True
            
            backtrack(path, used)
            
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


nums = [1, 2, 3]
print(permutations(nums))