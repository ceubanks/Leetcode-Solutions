from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit