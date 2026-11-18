class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = sorted([[p, s] for p,s in zip(position, speed)], reverse = True)
        fleets = 0
        slowest = 0

        for p, s in times:
            time = (target - p) / s
            if time > slowest:
                fleets += 1
                slowest = time
        
        return fleets