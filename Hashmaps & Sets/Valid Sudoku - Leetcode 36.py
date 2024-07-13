
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        def is_valid(unit: List[str]) -> bool:
            seen = set()
            for item in unit:
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
            return True
        
        for row in board:
            if not is_valid(row):
                return False
        
        for col in zip(*board):
            if not is_valid(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid(box):
                    return False
        
        return True