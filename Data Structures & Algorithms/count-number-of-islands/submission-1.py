class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            for rd, cd in directions:
                row = r + rd
                col = c + cd
                if row < 0 or row >= len(grid): continue
                if col < 0 or col >= len(grid[0]): continue
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    dfs(row, col)
        
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans