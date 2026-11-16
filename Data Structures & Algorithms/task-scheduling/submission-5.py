class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []

        for c in count.values():
            heapq.heappush_max(maxHeap, c)
        
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop_max(maxHeap) - 1
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time