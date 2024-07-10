
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in h:
                return [h[complement], i]
            h[num] = i

        return []
    
# Time: O(n)
# Space: O(n)