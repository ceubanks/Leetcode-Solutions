
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])
        ans = []

        i, j = 0, 0
        direction = RIGHT

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) < m * n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                direction = DOWN
                RIGHT_WALL -= 1
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                direction = LEFT
                DOWN_WALL -= 1
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                direction = UP
                LEFT_WALL += 1
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                direction = RIGHT
                UP_WALL += 1
        return ans
    
# Time: O(n * m)
# Space: O(n * m)