from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()

        for num in nums:
            if num in h:
                return True
            h.add(num)

        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)