N = 4

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def solve_queen(board, row):
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_queen(board, row + 1)


board = [-1] * N
solve_queen(board, 0)
