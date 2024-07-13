from typing import Counter, List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)