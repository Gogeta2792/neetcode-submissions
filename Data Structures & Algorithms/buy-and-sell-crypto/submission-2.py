class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_profit = prices[0], 0

        for sell in prices:
            buy = min(buy, sell)
            max_profit = max(max_profit, sell - buy)
        
        return max_profit