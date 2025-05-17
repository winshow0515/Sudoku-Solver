def print_sudoku(board):
    print("|-------+-------+-------|")
    for i in range(9):
        print("| ", end='')
        for j in range(9):
            print(board[i][j], end=" ")
            if j % 3 == 2:
                print("| ", end="")
        print()
        if i % 3 == 2:
            print("|-------+-------+-------|")

def read_board(path):
    with open(path, "r") as f:
        board = [list(line.strip()) for line in f.readlines()]
    return board
