
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> str:
        count = defaultdict(int)
        max_freq = 0
        L = 0

        for R in range(len(s)):
            curr_char = s[R]
            count[curr_char] += 1
            max_freq = max(max_freq, count[curr_char])

            while R - L + 1 - max_freq > k:
                count[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)

        return longest
