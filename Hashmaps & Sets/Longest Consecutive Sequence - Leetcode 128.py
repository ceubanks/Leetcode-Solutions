from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        s = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s:
                next_num = num + 1
                length = 1

                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        
        return longest