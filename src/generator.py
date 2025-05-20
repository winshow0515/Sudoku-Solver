import random
from util import print_sudoku
from solver import Solution

def sudoku_generator(holes):
    # Start with empty board
    board = [["." for _ in range(9)] for _ in range(9)]
    # Fill diagonal blocks (0, 4, 8 blocks in sudoku) in random
    for sx, sy in [(0, 0), (3, 3), (6, 6)]:
        # Fill 3x3 block
        to_be_filled = list(range(1, 10))
        random.shuffle(to_be_filled)
        for x in range(sx, sx + 3):
            for y in range(sy, sy + 3):
                board[x][y] = str(to_be_filled.pop())
        solution = Solution()
        solution.solveSudoku(board)

    to_be_delete = list(range(81))
    random.shuffle(to_be_delete)
    to_be_delete = to_be_delete[:holes]

    for i in to_be_delete:
        x, y = i // 9, i % 9
        board[x][y] = "."
    return board

if __name__ == "__main__":
    random.seed(3686)
    for idx, hole in enumerate([55, 55, 55, 60, 60, 60]):
        with open("../testcases/" + str(idx) + ".in", "w") as fout:
            board = sudoku_generator(hole)
            for row in board:
                print("".join(row), file=fout)#寫入檔案的方法(內容,檔案)