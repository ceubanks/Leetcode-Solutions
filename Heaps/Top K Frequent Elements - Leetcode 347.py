from collections import Counter
from heapq import heappush, heappushpop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, freq in count.items():
            if len(heap) < k:
                heappush(heap, (freq, key))
            else:
                heappushpop(heap, (freq, key))

        return [h[1] for h in heap]