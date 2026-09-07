class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_profit = prices[0], 0

        for price in prices:
            if price < buy:
                buy = price
            max_profit = max(max_profit, price - buy)
        
        return max_profit