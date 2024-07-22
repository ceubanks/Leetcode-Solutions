from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for i in range(n1):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True
        
        for i in range(n1, n2):
            s2_count[s2[i]] += 1
            s2_count[s2[i-n1]] -= 1

            if s2_count[s2[i-n1]] == 0:
                del s2_count[s2[i-n1]]

            if s2_count == s1_count:
                return True
            
        return False
    
    # Time: O(n)
    # Space: O(n)