
from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) == 0:
            return 0
        
        counter = Counter(text)
        balloon = 'balloon'

        if any(c not in counter for c in balloon):
            return 0
        
        return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])