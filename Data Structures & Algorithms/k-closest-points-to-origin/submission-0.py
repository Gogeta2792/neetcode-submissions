class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x, y = point[0], point[1]
            distance = (x ** 2 + y ** 2) ** (1/2)

            heapq.heappush_max(distances, (distance, point))

            if len(distances) > k:
                heapq.heappop_max(distances)
        
        res = []
        for distance in distances:
            res.append(distance[1])
        
        return res