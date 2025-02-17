from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 0:
            return
        
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # Time: O(n)
        # Space: O(1)
