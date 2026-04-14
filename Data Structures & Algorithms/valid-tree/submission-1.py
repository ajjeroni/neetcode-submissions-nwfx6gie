class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_neighbors = {i:[] for i in range(n)}
        for c,j in edges:
            node_neighbors[c].append(j)
            node_neighbors[j].append(c)
        
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in node_neighbors[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n