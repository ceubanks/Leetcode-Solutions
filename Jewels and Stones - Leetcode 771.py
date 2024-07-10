
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)

        count = 0

        for stone in S:
            if stone in s:
                count += 1

        return count