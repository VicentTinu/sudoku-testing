def solve_sudoku(board):
    # Input validation
    if not isinstance(board, list) or len(board) != 9:
        return None
    
    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            return None
        if not all(isinstance(x, int) and 0 <= x <= 9 for x in row):
            return None

    # Check if initial board is valid
    def is_valid(y, x, n):
        for i in range(9):
            if board[y][i] == n or board[i][x] == n:
                return False
        box_y, box_x = (y // 3) * 3, (x // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_y + i][box_x + j] == n:
                    return False
        return True

    def is_initial_board_valid():
        # Check rows
        for row in board:
            nums = [x for x in row if x != 0]
            if len(nums) != len(set(nums)):
                return False
        
        # Check columns
        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != 0]
            if len(nums) != len(set(nums)):
                return False
        
        # Check 3x3 boxes
        for box_y in range(0, 9, 3):
            for box_x in range(0, 9, 3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_y + i][box_x + j]
                        if val != 0:
                            nums.append(val)
                if len(nums) != len(set(nums)):
                    return False
        return True

    if not is_initial_board_valid():
        return None

    def solve():
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for n in range(1, 10):
                        if is_valid(y, x, n):
                            board[y][x] = n
                            if solve():
                                return True
                            board[y][x] = 0
                    return False
        return True

    # Create a copy of the board to avoid modifying the input
    board = [row[:] for row in board]
    
    # Try to solve the puzzle
    if solve():
        return board
    return None
