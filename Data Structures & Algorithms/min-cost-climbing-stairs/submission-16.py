class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        one, two = cost[-1], 0

        for i in range(len(dp) - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        
        return min(one, two)