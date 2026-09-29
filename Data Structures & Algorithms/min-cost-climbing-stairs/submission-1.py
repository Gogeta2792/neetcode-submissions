class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        
        def helper(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            return memo[i]
        
        helper(0)

        return min(memo[0], memo[1])