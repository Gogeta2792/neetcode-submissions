class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one, two = cost[len(cost) - 2], cost[len(cost) - 1]

        for i in range(len(cost) - 3, -1, -1):
            tmp = cost[i] + min(one, two)
            two = one
            one = tmp

        return min(one, two)