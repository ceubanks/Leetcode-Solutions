
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while  i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                ans.append(f'{start}->{nums[i]}')
            else:
                ans.append(f'{start}')

            i += 1
        
        return ans
    
# Time: O(n)
# Space: O(1)