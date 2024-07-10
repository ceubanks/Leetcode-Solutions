# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0

        i = 0
        while i < len(s):
            current_roman_num = roman[s[i]]
            if i+1 < len(s):
                next_roman_num = roman[s[i+1]]

                if current_roman_num >= next_roman_num:
                    sum += current_roman_num
                    i += 1
                else:
                    converted_roman_num = next_roman_num - current_roman_num
                    sum += converted_roman_num
                    i += 2
            else:
                sum += current_roman_num
                i += 1

        return sum

# Time: O(n)
# Space: O(1)