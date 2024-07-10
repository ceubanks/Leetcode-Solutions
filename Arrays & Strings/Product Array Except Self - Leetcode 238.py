from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        l_mult = 1
        r_mult = 1

        n = len(nums)

        l_arr = [1] * n
        r_arr = [1] * n

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]
    
# Time: O(n)
# Space: O(1)