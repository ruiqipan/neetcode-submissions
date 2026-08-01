class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        ans = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                ans += 1
        return ans