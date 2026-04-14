from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #declaring variables 
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()
        queue = deque()
        length = 0

        #append the first position
        queue.append((0, 0))
        visited.add((0, 0))

        #start our bfs
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == (ROWS - 1, COLUMNS - 1):
                    return length
                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc)) < 0 or r + dr == ROWS or c + dc == COLUMNS or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1:
                        continue 
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1

        return -1 