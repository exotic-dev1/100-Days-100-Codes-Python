"""
Day100 :- Generate Parentheses
Difficulty :- Medium
Concepts :- backtracking, recursion, pruning
"""
def generateParenthesis(n):
    result = []

    def backtrack(curr, openCount, closeCount):

        
        if len(curr) == 2 * n:
            result.append(curr)
            return

       
        if openCount < n:
            backtrack(curr + "(", openCount + 1, closeCount)
            
        if closeCount < openCount:
            backtrack(curr + ")", openCount, closeCount + 1)

    backtrack("", 0, 0)
    return result

print(generateParenthesis(2))