def solveNQueens(n: int, initialX: int, initialY: int):
    if initialX < 0 or initialX >= n or initialY < 0 or initialY >= n:
        return "Invalid initial position"

    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[initialX][initialY] = 'Q'
    
    # Helper function to check if placing a queen is safe
    def isSafe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check positive diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        # Check negative diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        return True
    
    # Backtracking function to place queens
    def backtrack(row):
        if row == n:
            res.append([''.join(r) for r in board])
            return True
        
        if row == initialX:  # Skip the row with the initial queen
            return backtrack(row + 1)
        
        for col in range(n):
            if isSafe(row, col):
                board[row][col] = 'Q'
                if backtrack(row + 1):
                    return True
                board[row][col] = '.'

        return False
    
    if not backtrack(0):
        return "No solution found"
    
    return res

def printSolutions(boards):
    if isinstance(boards, str):
        print(boards)
    elif not boards:
        print("No solution found!")
    else:
        for idx, board in enumerate(boards):
            print(f"Solution {idx + 1}:")
            for row in board:
                print(' '.join(row))
            print()

if __name__ == "__main__":
    n = int(input("Enter N: "))
    if n < 4:
        print("No Solutions for NQueens when N<4, N should be at least 4!")
    else:
        i, j = map(int, input("Enter coordinate of first queen (i,j) starting from (0,0): ").split(','))
        boards = solveNQueens(n, i, j)
        printSolutions(boards)
