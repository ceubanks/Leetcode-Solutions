
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans, res = [], []

        def _backtrack(current_sum, index) -> None:
            if current_sum == target:
                ans.append(res[:])
                return

            for i in range(index, n):
                num = candidates[i]
                current_sum += num                
                if current_sum <= target:
                    res.append(num)
                    _backtrack(current_sum, i)
                    res.pop()
                
                current_sum -= num

        _backtrack(0, 0)
        return ans
                