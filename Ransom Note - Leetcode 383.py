
from collections import Counter, defaultdict


class Solution:
    def checkRansomNote(self, ransomNote: str, counter: dict) -> bool:
        for r in ransomNote:
            if r not in counter:
                return False
            elif counter[r] == 1:
                del counter[r]
            else:
                counter[r] -= 1
        
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for m in magazine:
            if m in counter:
                counter[m] += 1
            else:
                counter[m] = 1
        
        return self.checkRansomNote(ransomNote, counter)
    
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)

        for m in magazine:
            counter[m] += 1

        return self.checkRansomNote(ransomNote, counter)
    
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        return self.checkRansomNote(ransomNote, counter)
