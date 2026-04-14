from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #initialize variables
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        islands = 0
        visited = set()
        
        #our bfs function
        def bfs(grid, row, column):
            
            queue = deque()
            queue.append((row, column))
            visited.add((row, column))

            while len(queue) > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                    for dr, dc in neighbors:
                        if(min(r + dr, c + dc)) < 0 or r + dr == ROWS or c + dc == COLUMNS or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == "0":
                            continue
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

 

        #traverse through the grid
        for r in range(ROWS):
            for c in range(COLUMNS):
                #if it's water then go next
                if grid[r][c] == "0":
                    continue
                #if it's land
                #have we visited this before?
                #go next if we have
                if grid[r][c] == "1" and (r, c) in visited:
                    continue 
                #if not
                #add to islands 
                #call bfs
                islands += 1
                bfs(grid, r, c)
        #after we finish going through the grid we return islands
        return islands 