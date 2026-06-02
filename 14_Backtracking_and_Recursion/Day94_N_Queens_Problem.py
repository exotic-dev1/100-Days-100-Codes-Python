"""
Day94 :- N Queens
Difficulty :- Hard
Concepts :- backtracking, recursion, constraint satisfaction
"""
def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        
        for i in range(row):
            if board[i][col] == 'Q':
                return False
                
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            solutions.append([''.join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions


# Example
n = 4
solutions = solve_n_queens(n)

print(f"Number of solutions: {len(solutions)}\n")
for solution in solutions:
    for row in solution:
        print(row)
    print()