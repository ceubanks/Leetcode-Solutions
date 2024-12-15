
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
    
    '''
    This backtracking algorithm is designed to determine if a given word can be found in a 2D grid of characters. 
    The algorithm explores all possible paths in the grid to find the word, using depth-first search (DFS) to 
    backtrack when a path does not lead to a solution.

    The algorithm starts by iterating over each cell in the grid. For each cell, if the character matches the 
    first character of the word, it initiates a DFS from that cell. The DFS function, `_dfs`, is responsible 
    for exploring all possible directions (up, down, left, right) from the current cell.

    The DFS function checks the following conditions:
    1. If the current word index matches the length of the word, it means the entire word has been found, 
       and the function returns True.
    2. If the current cell is out of bounds, already visited, or does not match the current character of the word, 
       the function returns False.

    If the current cell is valid, it marks the cell as visited and recursively calls the DFS function for the 
    neighboring cells. If any of the recursive calls return True, it means the word has been found, and the 
    function returns True. Otherwise, it backtracks by unmarking the cell as visited and returns False.

    The main function, `exist`, iterates over each cell in the grid and calls the DFS function for cells that 
    match the first character of the word. If any of the DFS calls return True, the function returns True, 
    indicating that the word exists in the grid. If no path is found, the function returns False.

    This algorithm has a time complexity of O(N * 4^L), where N is the number of cells in the grid and L is the 
    length of the word. The space complexity is O(L) due to the recursion stack used by the DFS function.
    
    Time Complexity: O(N * 4^L)
    Space Complexity: O(L)  
    '''
    def exist_2(self, grid: List[List[str]], word: str) -> bool:
        def is_valid(row, col, index):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]) and 
                    index < len(word) and grid[row][col] != '#' and 
                    word[index] == grid[row][col])

        def backtrack(row, col, index):
            if index == len(word):
                return True
            if not is_valid(row, col, index):
                return False
            
            temp, grid[row][col] = grid[row][col], '#'
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if backtrack(row + dx, col + dy, index + 1):
                    return True
            grid[row][col] = temp
            return False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == word[0] and backtrack(row, col, 0):
                    return True
        return False
    