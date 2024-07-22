from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], hr: int) -> int:
        def k_works(k: int) -> bool:
            h = 0
            for p in piles:
                h += ceil(p / k)
            return h <= hr
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            if k_works(mid):
                r = mid
            else:
                l = mid + 1
        
        return l