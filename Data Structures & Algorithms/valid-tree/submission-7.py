class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(prev, curr):
            if curr in visited:
                return False
            
            visited.add(curr)

            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(curr, nei):
                    return False
            
            return True
        
        return dfs(-1, 0) and len(visited) == n