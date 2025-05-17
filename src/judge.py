from solver import Solution
from util import read_board

if __name__ == "__main__":
    import time

    fmt = "| {: ^20s} | {: ^12s} | {: ^11s} | {: ^20s} |"
    print(fmt.format("testcases", "# of holes", "time", "# of tries"))
    print(fmt.format("-"*18, "-"*12, "-"*11, "-"*20))
    for i in range(6):
        file_path = f"../testcases/{i}.in"
        board = read_board(file_path)
        solution = Solution()

        holes = sum([line.count(".") for line in board])
        # Start timing
        start = time.monotonic()
        solution.solveSudoku(board)

        time_cost = time.monotonic() - start
        print(fmt.format(f"`{file_path}`", str(holes), "%.4f" % time_cost + "s", str(solution.cnt)))
