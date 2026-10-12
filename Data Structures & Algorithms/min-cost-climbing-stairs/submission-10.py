class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = cost[-1]
        one = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        
        return min(one, two)