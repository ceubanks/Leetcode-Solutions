
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        found = [False]
        def _dfs(i, j, word_index):
            if len(word) == word_index:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[word_index] or visited[i][j]:
                return False
            
            visited[i][j] = True
            word_index += 1
            found[0] = (_dfs(i+1, j, word_index) or
                             _dfs(i, j+1, word_index) or
                             _dfs(i-1, j, word_index) or 
                             _dfs(i, j-1, word_index))
            visited[i][j] = False
            return found[0]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and _dfs(i, j, 0):
                    return True
                
        return False