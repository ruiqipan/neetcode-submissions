class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            while q:
                curr = q.pop()
                for nei in adj[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
        
        ans = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                bfs(node)
                ans += 1
        return ans