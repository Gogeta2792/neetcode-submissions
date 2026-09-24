class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0

        while start < n:
            position = start
            stations = n
            car_gas = 0

            while car_gas >= 0:
                car_gas += gas[position] - cost[position]
                position = 0 if position + 1 ==n else position + 1
                stations -= 1
                if stations == 0 and car_gas >= 0:
                    return start
            
            start += n - stations
            
        return -1