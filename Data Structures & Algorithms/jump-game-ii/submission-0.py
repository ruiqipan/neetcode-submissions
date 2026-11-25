class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if i >= n - 1:
                return 0
            if memo[i] != -1:
                return memo[i]

            best = float("inf")
            max_jump = min(nums[i], n - 1 - i)
            for j in range(1, max_jump + 1):
                best = min(best, 1 + dfs(i + j))
            memo[i] = best
            return memo[i]

        return dfs(0)
