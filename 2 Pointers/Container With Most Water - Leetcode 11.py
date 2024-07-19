
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            current_max_height = max(height[left], height[right])
            current_width = right - left
            current_area = current_width * current_max_height

            max_area = max(max_area, current_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_area
    
# Time: O(n)
# Space: O(1)