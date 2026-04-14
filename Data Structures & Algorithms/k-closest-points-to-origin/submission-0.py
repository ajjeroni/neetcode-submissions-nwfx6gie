import heapq

class heapPoint:
    def __init__(self, distance, index):
        self.distance = distance
        self.index = index
    def __lt__(self, other):
        return self.distance < other.distance
    def __repr__(self):
        return str(self.index)
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1:
            return points
        heap = []
        
        for i,point in enumerate(points):
            x,y = point
            distance = (math.sqrt(x**2 + y**2))
            pObj = heapPoint(-distance, i)
            heapq.heappush(heap, pObj)
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            i = heapq.heappop(heap).index
            res.append(points[i])
        return res
        
        

        
            