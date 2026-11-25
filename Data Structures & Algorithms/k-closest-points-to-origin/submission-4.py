class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush_max(maxHeap, [distance, point])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        return [point for distance, point in maxHeap]
