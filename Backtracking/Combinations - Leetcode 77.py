
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, res = [], []

        def _backtrack(i):
            if len(res) == k:
                ans.append(res[:])
                return
            
            if i > n:
                return
            
            # pick this element
            res.append(i)
            _backtrack(i+1)

            res.pop()

            # don't pick this element
            _backtrack(i+1)

        _backtrack(1)
        return ans