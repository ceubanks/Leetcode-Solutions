# https://leetcode.com/problems/find-closest-number-to-zero/

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for num in nums:
            if abs(num) < abs(closest):
                closest = num

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        
        return closest

# Time: O(n)
# Space: O(1)