"""
Day97 :- Palindrome Partitioning
Difficulty :- Medium
Concepts :- backtracking, recursion, strings
"""
def partition(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result

s = "aab"
print(partition(s))
    
