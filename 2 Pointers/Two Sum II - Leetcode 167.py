from typing import List

class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        # Time: O(n)
        # Space: O(1)