from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        left, right = 0, total - 1

        while left <= right:
            mid = (left + right) // 2

            # calculate row and column indices
            row, col = divmod(mid, cols)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False