from collections import Counter
import heapq
from typing import List

'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        heap = [(-count, word) for word, count in counter.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
    
    
