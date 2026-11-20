class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adj = defaultdict(list)

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
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
        
        return dfs(-1,0) and len(visited) == n