class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)

        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                task = heapq.heappop_max(maxHeap) - 1
                if task:
                    q.append((task, time + n))
            
            if q and q[0][1] == time:
                val, i = q.popleft()
                heapq.heappush_max(maxHeap, val)
        
        return time