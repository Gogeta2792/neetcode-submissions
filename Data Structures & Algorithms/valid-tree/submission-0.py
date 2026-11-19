class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        def dfs(prev_node, node):
            if node in visited:
                return False
            
            visited.add(node)
            for j in adj[node]:
                if j == prev_node:
                    continue
                if not dfs(node, j):
                    return False
            
            return True
        
        return dfs(-1, 0) and n == len(visited)