
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        min_len = float('inf')
        summ = 0

        for r in range(n):
            summ += nums[r]

            while summ >= s and l <= r:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l += 1
        
        return min_len if min_len <= n else 0