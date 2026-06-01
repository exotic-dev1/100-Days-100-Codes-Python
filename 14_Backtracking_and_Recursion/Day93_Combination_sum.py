"""
Day93 :- Combination Sum
Difficulty :- Medium
Concepts :- backtracking, recursion
"""
def combinationSum(candidates, target):
    result = []

    def backtrack(start, current_combination, remaining):
        
        if remaining == 0:
            result.append(current_combination[:])
            return
        
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            
            backtrack(i, current_combination, remaining - candidates[i])
            
            current_combination.pop()

    backtrack(0, [], target)
    return result
    
candidates = [2, 3, 6, 7]
target = 7

print(combinationSum(candidates, target))