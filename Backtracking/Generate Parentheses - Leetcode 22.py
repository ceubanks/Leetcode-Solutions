
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, res = [], []

        def _backtrack(left, right):
            if len(res) == n*2:
                ans.append(''.join(res))
                return
            
            if left < n:
                res.append('(')
                _backtrack(left+1, right)
                res.pop()
            if right < left:
                res.append(')')
                _backtrack(left, right+1)
                res.pop()
            
        _backtrack(0, 0)
        return ans