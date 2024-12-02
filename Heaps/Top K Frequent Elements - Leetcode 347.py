from collections import Counter
from heapq import heappush, heappop, heappushpop
from typing import List

'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for word, count in counter.items():
            heappush(heap, (count, word))

            if len(heap) > k:
                heappop(heap)
        
        return [word for count, word in heap]   
    
    # Time: O(n * logk)
    # Space: O(k)