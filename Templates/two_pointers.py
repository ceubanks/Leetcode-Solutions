from typing import List, Tuple, Optional

class TwoPointers:
    """
    A collection of two pointer pattern implementations.
    Used for problems involving sorted arrays or when we need to find pairs
    that satisfy certain conditions.
    """
    
    @staticmethod
    def opposite_ends(arr: List[int], target: int) -> List[Tuple[int, int]]:
        """
        Template for two pointers starting from opposite ends.
        Common in problems like two sum, container with most water, etc.
        
        Args:
            arr: Sorted input array
            target: Target value to find/compare
            
        Returns:
            List of pairs that meet the target condition
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(arr) - 1
        results = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum == target:
                results.append((arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return results
    
    @staticmethod
    def same_direction(arr: List[int]) -> List[int]:
        """
        Template for two pointers moving in the same direction.
        Common in problems like removing duplicates, finding triplets, etc.
        
        Args:
            arr: Input array
            
        Returns:
            Modified array or results based on problem
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize slow pointer (usually for placing elements)
        slow = 0
        
        # Fast pointer iterates through array
        for fast in range(1, len(arr)):
            # Compare elements and move slow pointer when condition is met
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
                
        # Return modified array up to slow + 1 (new length)
        return arr[:slow + 1]
    
    @staticmethod
    def three_pointers(arr: List[int], target: int) -> List[Tuple[int, int, int]]:
        """
        Template for problems requiring three pointers.
        Common in problems like 3Sum, triplet sum close to target, etc.
        
        Args:
            arr: Sorted input array
            target: Target value to find/compare
            
        Returns:
            List of triplets that meet the target condition
            
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        arr.sort()  # Ensure array is sorted
        results = []
        
        for i in range(len(arr) - 2):
            # Skip duplicates for i
            if i > 0 and arr[i] == arr[i - 1]:
                continue
                
            left = i + 1
            right = len(arr) - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    results.append((arr[i], arr[left], arr[right]))
                    
                    # Skip duplicates for left and right
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return results

# Example usage
if __name__ == "__main__":
    # Opposite ends example (Two Sum II)
    sorted_arr = [2, 7, 11, 15]
    target = 9
    print(f"Pairs summing to {target}:", TwoPointers.opposite_ends(sorted_arr, target))
    
    # Same direction example (Remove Duplicates)
    arr_with_duplicates = [1, 1, 2, 2, 3, 4, 4, 5]
    print("Array after removing duplicates:", TwoPointers.same_direction(arr_with_duplicates))
    
    # Three pointers example (3Sum)
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(f"Triplets summing to {target}:", TwoPointers.three_pointers(arr, target)) 