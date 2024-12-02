from typing import List, Tuple

class MergeIntervals:
    """
    A collection of merge intervals pattern implementations.
    Used for problems involving intervals, scheduling, and overlapping ranges.
    """
    
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        """
        Template for merging overlapping intervals.
        
        Args:
            intervals: List of intervals [start, end]
            
        Returns:
            List of merged intervals
            
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return []
            
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                # Overlapping intervals, update end time
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                # Non-overlapping interval, add to result
                merged.append(interval)
                
        return merged
    
    @staticmethod
    def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Template for inserting a new interval into existing intervals.
        
        Args:
            intervals: List of non-overlapping intervals
            new_interval: Interval to insert
            
        Returns:
            List of merged intervals after insertion
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        merged = []
        i = 0
        n = len(intervals)
        
        # Add all intervals before new_interval
        while i < n and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1
            
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
            
        merged.append(new_interval)
        
        # Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1
            
        return merged
    
    @staticmethod
    def find_intersection(intervals1: List[List[int]], intervals2: List[List[int]]) -> List[List[int]]:
        """
        Template for finding intersection of two interval lists.
        
        Args:
            intervals1: First list of intervals
            intervals2: Second list of intervals
            
        Returns:
            List of intersecting intervals
            
        Time Complexity: O(n + m)
        Space Complexity: O(min(n, m))
        """
        result = []
        i = j = 0
        
        while i < len(intervals1) and j < len(intervals2):
            # Find overlapping interval
            start = max(intervals1[i][0], intervals2[j][0])
            end = min(intervals1[i][1], intervals2[j][1])
            
            if start <= end:
                result.append([start, end])
                
            # Move pointer of interval with smaller end time
            if intervals1[i][1] < intervals2[j][1]:
                i += 1
            else:
                j += 1
                
        return result

# Example usage
if __name__ == "__main__":
    # Merge intervals example
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    print("Merged intervals:", MergeIntervals.merge(intervals))
    
    # Insert interval example
    intervals = [[1,3], [6,9]]
    new_interval = [2,5]
    print("After inserting interval:", MergeIntervals.insert_interval(intervals, new_interval))
    
    # Find intersection example
    intervals1 = [[0,2], [5,10], [13,23], [24,25]]
    intervals2 = [[1,5], [8,12], [15,24], [25,26]]
    print("Intersecting intervals:", MergeIntervals.find_intersection(intervals1, intervals2)) 