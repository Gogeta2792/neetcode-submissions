class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[p,s] for p, s in zip(position, speed)])
        arrival = []

        for p, s in cars[::-1]:
            arrival.append((target - p) / s)
            if len(arrival) >= 2 and arrival[-1] <= arrival[-2]:
                arrival.pop()
        
        return len(arrival)