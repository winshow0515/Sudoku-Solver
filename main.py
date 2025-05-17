from typing import List
class Solution:
    def getPossibilities(self, board, x, y):
        possibles = set("123456789")
        for i in range(9):
            possibles.discard(board[i][y])
            possibles.discard(board[x][i])
            possibles.discard(board[x//3*3 + i//3][y//3*3 + i%3])
        return possibles
    
    def solveSudoku(self, board: List[List[str]], start=0) -> None:
        """
        Do not return anything, modify board in-place instead.
        """    
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