# Sudoku-Solver
a fast sudoku solver and generator!

## generator.py
* `sudoku_generator(holes)`

    將1~9的數字以隨機順序填滿左上、中間、右下的九宮格，在呼叫solveSudoku()填滿board，最後依照參數holes隨機挖出要求的空格數
    ```python
    board = sudoku_generator(36)
    ...
    ```

### 使用方法

先創建一個名為testcases的空資料夾，在終端執行generator.py即可生成測資

可更改第29行的random.seed()裡的數字產生不同的隨機測資
```python
random.seed(3686) #-> random.seed(1)
```

也可更改第30行決定測資數量和測資要挖幾個洞
```python
for idx, hole in enumerate([55, 55, 55, 60, 60, 60]):
#for idx, hole in enumerate([1, 2, 3]):
```
## Solver.py
* `getPossibilities(self, board, x, y)` 

    回傳board[x][y]能放的數字

* `solveSudoku(self, board: List[List[str]], start=0)` 

    用 DFS回溯法搭配 `getPossibilities()` 來完成數獨

``` python
from src.solver import Solution
solution = Solution()
solution.solveSudoku(board)
...
```
## util.py
* `print_sudoku(board)`

    開發過程中用來輸出board函式
* `read_board(path)`

    讀取測資檔的函式

## judge.py
讀入testcases資料夾裡的測資，並呼叫 `solveSudoku()` 完成數獨，輸出如以下的 Testing

## Testing

|      testcases       |  # of holes  |    time     |      # of tries      |
|  ------------------  | ------------ | ----------- | -------------------- |
| `../testcases/0.in`  |      55      |   0.1410s   |        43352         |
| `../testcases/1.in`  |      55      |   1.3750s   |        404323        |
| `../testcases/2.in`  |      55      |   0.6410s   |        236894        |
| `../testcases/3.in`  |      60      |   0.9060s   |        277301        |
| `../testcases/4.in`  |      60      |   0.5470s   |        132324        |
| `../testcases/5.in`  |      60      |   0.0000s   |         130          |