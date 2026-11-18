class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = sorted([[p, s] for p,s in zip(position, speed)], reverse = True)
        stack = []

        for p, s in times:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)