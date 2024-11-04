def is_safe(board, row, col, n):
    # Check column for any queen
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        return True  # All queens are placed successfully

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_n_queens_util(board, row + 1, n):  # Recur to place the rest
                return True
            board[row][col] = 0  # Backtrack if placing queen here doesn't work

    return False

def solve_n_queens(n, first_queen_column):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][first_queen_column] = 1  # Place the first queen in the specified column of the first row

    # Start solving from the second row
    if not solve_n_queens_util(board, 1, n):
        print("No solution is available")
    else:
        # Print the solution board
        for row in board:
            print(row)

# Get user inputs for the size of the board and starting position of the first queen
n = int(input("Enter the size of the board (n): "))
first_queen_column = int(input(f"Enter the starting position of the first queen (column index between 0 and {n - 1}): "))

# Solve the n-Queens problem
solve_n_queens(n, first_queen_column)
