class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [0] * len(gas)
        delta_sum = 0

        for i in range(len(gas)):
            delta[i] = gas[i] - cost[i]
            delta_sum += delta[i]

        if delta_sum < 0:
            return -1

        total = 0
        start = 0

        for idx, ele in enumerate(delta):
            total += ele
            if total < 0:
                total = 0
                start = idx + 1
        
        return start
