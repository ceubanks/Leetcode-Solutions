
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 0
        l = 0
        n = len(s)
        char_set = set()

        for r in range(n):
            curr_char = s[r]
            while curr_char in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(curr_char)
            max_len = max(max_len, len(char_set))
        
        return max_len
    
    # Time: O(n)
    # Space: O(min(n, m)) or O(1)