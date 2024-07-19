from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                return ans
            
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return ans
    
        # Time: O(n^2)
        # Space: O(1)