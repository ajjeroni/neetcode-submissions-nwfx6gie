class PointWrapper:
    def __init__(self, points, distance):
        self.points = points
        self.distance = distance
    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt((x ** 2) + (y ** 2))
            obj = PointWrapper(point, distance)
            heapq.heappush(heap, obj)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).points)

        return res