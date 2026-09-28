class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        car_gas = 0

        for i in range(len(gas)):
            car_gas += gas[i] - cost[i]
            if car_gas < 0:
                car_gas = 0
                start = i + 1
        
        return start