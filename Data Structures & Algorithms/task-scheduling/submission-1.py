from collections import deque
import heapq

class taskObj:
    def __init__(self, task, freq):
        self.task = task
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq
    
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}
        heap = []
        dq = deque()
        cycle = 0

        for task in tasks:
            freq[task] = freq.get(task, 0) - 1
        
        for task, count in freq.items():
            obj = taskObj(task, count)
            heapq.heappush(heap, obj)

        while heap or dq:

            if dq and dq[0][0] == cycle:
                obj = dq.popleft()[1]
                heapq.heappush(heap, obj)
                
            
            if not heap:
                # print('idle')
                cycle += 1
                continue

            obj = heapq.heappop(heap)
            # print('heap', obj.task)
            obj.freq += 1
            if obj.freq < 0:
                dq.append((cycle + n + 1, obj))
            cycle += 1
        
        return cycle







