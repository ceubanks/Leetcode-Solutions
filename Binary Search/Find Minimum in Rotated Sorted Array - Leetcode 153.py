from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]
    
    # Time: O(logn)
    # Space: O(1)