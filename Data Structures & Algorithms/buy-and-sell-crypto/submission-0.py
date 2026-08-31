class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            best_profit = max(best_profit, price - lowest)
        
        return best_profit