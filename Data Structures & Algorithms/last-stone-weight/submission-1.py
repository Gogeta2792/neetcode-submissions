class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            tmp = abs(-heapq.heappop(max_heap) - -heapq.heappop(max_heap))
            if tmp != 0:
                heapq.heappush(max_heap, -tmp)
        
        return -max_heap[0] if max_heap else 0