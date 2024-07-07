class Solution:
    def isSubsequence(self, s:str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == '':
            return True
        
        s_counter, t_counter = 0, 0
        while s_counter < len(s) and t_counter < len(t):
            if s[s_counter] == t[t_counter]:
                s_counter += 1
            t_counter += 1

        return s_counter == len(s)

