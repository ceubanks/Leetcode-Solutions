from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        min_len = float('inf')
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
            
        i = 0
        while i < min_len:
            if any(s[i] != strs[0][i] for s in strs):
                return s[:i]
            i += 1
        
        return s[:i]
            