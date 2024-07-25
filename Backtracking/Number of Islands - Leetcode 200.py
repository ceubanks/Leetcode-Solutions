from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        num_islands = 0

        def _check_island(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            _check_island(i+1, j)
            _check_island(i, j+1)
            _check_island(i-1, j)
            _check_island(i, j-1)

        for i in range(m):
            for j in range(n):
                if [grid[i][j]] == '1':
                    num_islands += 1
                    _check_island(i, j)

        return num_islands