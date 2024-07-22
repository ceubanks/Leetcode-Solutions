from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        # Find minimum element in the array as pivot element

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        # Minimum index is now at L
        min_index = L

        # Change L and R to the correct range
        if min_index == 0:
            L, R = 0, n - 1
        elif nums[0] <= target and target <= nums[min_index - 1]:
            L, R = 0, min_index - 1
        else:
            L, R = min_index, n - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1 