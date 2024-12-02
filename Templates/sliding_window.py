from typing import List, Dict, Any
from collections import defaultdict

class SlidingWindow:
    """
    A collection of sliding window pattern implementations.
    Used for problems involving arrays/strings where we need to find/calculate
    something among all contiguous subarrays of a given size.
    """
    
    @staticmethod
    def fixed_size_window(arr: List[Any], k: int) -> List[Any]:
        """
        Template for fixed-size sliding window problems.
        
        Args:
            arr: Input array/string
            k: Size of the window
            
        Returns:
            List containing results for each valid window
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr or k <= 0:
            return []
            
        window_start = 0
        results = []
        current_window = []  # Or use other data structure based on problem
        
        for window_end in range(len(arr)):
            # 1. Add element to window
            current_window.append(arr[window_end])
            
            # 2. If window size equals k, process window and slide
            if window_end >= k - 1:
                results.append(current_window.copy())  # Or process window differently
                current_window.remove(arr[window_start])
                window_start += 1
                
        return results
    
    @staticmethod
    def variable_size_window(arr: List[Any], target: Any) -> List[Any]:
        """
        Template for variable-size sliding window problems.
        
        Args:
            arr: Input array/string
            target: Target value or condition
            
        Returns:
            List containing results that meet the target condition
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        window_start = 0
        results = []
        current_sum = 0  # Or other metric based on problem
        
        for window_end in range(len(arr)):
            # 1. Add element to window
            current_sum += arr[window_end]
            
            # 2. Shrink window while condition is violated
            while current_sum > target:  # Adjust condition as needed
                current_sum -= arr[window_start]
                window_start += 1
                
            # 3. Process window if needed
            if current_sum == target:  # Adjust condition as needed
                results.append(arr[window_start:window_end + 1])
                
        return results

    @staticmethod
    def string_window(s: str, pattern: str) -> Dict[str, Any]:
        """
        Template for string-based sliding window problems.
        
        Args:
            s: Input string
            pattern: Pattern to match
            
        Returns:
            Dictionary containing results (e.g., min window, count, etc.)
            
        Time Complexity: O(n)
        Space Complexity: O(k) where k is size of character set
        """
        window_start = 0
        char_frequency = defaultdict(int)
        matches = 0
        result = {"start": 0, "length": float('inf')}
        
        # Build pattern frequency map
        pattern_freq = defaultdict(int)
        for char in pattern:
            pattern_freq[char] += 1
            
        for window_end in range(len(s)):
            # 1. Add character to window
            right_char = s[window_end]
            if right_char in pattern_freq:
                char_frequency[right_char] += 1
                if char_frequency[right_char] == pattern_freq[right_char]:
                    matches += 1
                    
            # 2. Shrink window if possible
            while matches == len(pattern_freq):
                # Update result if current window is smaller
                window_length = window_end - window_start + 1
                if window_length < result["length"]:
                    result["start"] = window_start
                    result["length"] = window_length
                
                # Remove left character
                left_char = s[window_start]
                if left_char in pattern_freq:
                    if char_frequency[left_char] == pattern_freq[left_char]:
                        matches -= 1
                    char_frequency[left_char] -= 1
                    
                window_start += 1
                
        return result

# Example usage
if __name__ == "__main__":
    # Fixed size window example
    arr = [1, 2, 3, 4, 5]
    k = 3
    print(f"Fixed size windows of {k}:", SlidingWindow.fixed_size_window(arr, k))
    
    # Variable size window example
    arr = [1, 7, 4, 3, 1, 2, 1, 5, 1]
    target = 7
    print(f"Subarrays summing to {target}:", SlidingWindow.variable_size_window(arr, target))
    
    # String window example
    s = "ADOBECODEBANC"
    pattern = "ABC"
    result = SlidingWindow.string_window(s, pattern)
    if result["length"] != float('inf'):
        min_window = s[result["start"]:result["start"] + result["length"]]
        print(f"Minimum window containing {pattern}: {min_window}") 