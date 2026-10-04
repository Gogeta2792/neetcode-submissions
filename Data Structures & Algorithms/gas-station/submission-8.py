class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currCost, start = 0, 0

        if sum(cost) > sum(gas):
            return -1

        for i in range(len(gas)):
            currCost += gas[i] - cost[i]
            if currCost < 0:
                start = i + 1
                currCost = 0
        
        return start