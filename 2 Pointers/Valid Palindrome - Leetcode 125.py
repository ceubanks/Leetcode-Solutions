
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        s_cleaned = ''.join(c for c in s if c.isalnum())
        return s_cleaned == s_cleaned[::-1]