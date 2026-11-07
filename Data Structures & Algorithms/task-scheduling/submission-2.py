class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        if n == 0:
            return sum(count.values())

        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)
        q = deque()

        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = heapq.heappop_max(maxHeap) - 1
                if val:
                    q.append((val, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time