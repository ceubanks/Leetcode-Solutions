
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        s_counter, t_counter = Counter(s), Counter(t)

        return s_counter == t_counter
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        return sorted(s) == sorted(t)