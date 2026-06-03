"""
Day95 :- Sudoku Solver
Difficulty :- Hard
Concepts :- backtracking, recursion, constraint satisfaction
"""
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def is_valid(board, num, pos):
    row, col = pos

    for c in range(9):
        if board[row][c] == num and c != col:
            return False

    for r in range(9):
        if board[r][col] == num and r != row:
            return False

    box_row = row // 3
    box_col = col // 3

    for r in range(box_row * 3, box_row * 3 + 3):
        for c in range(box_col * 3, box_col * 3 + 3):
            if board[r][c] == num and (r, c) != pos:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if not empty:
        return True 

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0 

    return False

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists")