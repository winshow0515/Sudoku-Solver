from typing import List
class Solution:
    def __init__(self):
        self.cnt = 0
    def getPossibilities(self, board, x, y):
        possibles = set("123456789")
        for i in range(9):
            possibles.discard(board[i][y])
            possibles.discard(board[x][i])
            possibles.discard(board[x//3*3 + i//3][y//3*3 + i%3])
        return sorted(possibles)
    
    def solveSudoku(self, board: List[List[str]], start=0) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.cnt += 1    
        if start == 81:
            return True
        x, y = start//9, start%9
        if board[x][y] != '.':
            return self.solveSudoku(board, start+1)
        
        for guess in self.getPossibilities(board, x, y):
            board[x][y] = guess
            if self.solveSudoku(board, start+1):
                return True
            board[x][y] = '.'
        return False

# doulbe under - dunder
if __name__ == "__main__":

    fout = open("tmp.txt", "w")
    fout.write("HI")
    fout.close()

    fin = open("tmp.txt", "r")
    s = fin.read()
    print(s)
    fin.close()

    with open("tmp.txt", "w") as fout:
        fout.write("HI")

    with open("tmp.txt", "r") as fin:
        print(fin.read())