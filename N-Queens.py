def queens(n):
    def valid(board, row, col):
        return all(board[r] != col and abs(board[r] - col) != row - r for r in range(row))

    def print_state(state, board):
        print(state)
        for row in range(n):
            for col in range(n):
                if board[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def backtrack(state, board, row):
        if row == n:
            print_state("Final configuration", board)
            return
        for col in range(n):
            if valid(board, row, col):
                board[row] = col
                print_state("Next state", board)
                backtrack(state, board, row + 1)
                board[row] = -1

    board = [-1] * n
    print_state("Start state", board)
    backtrack("Start state", board, 0)

# N-Queens
n = int(input("Number of queens: "))
queens(n)
