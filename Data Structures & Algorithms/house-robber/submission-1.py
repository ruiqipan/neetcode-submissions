class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            robCurrent = dfs(i + 2) + nums[i]
            robNext = dfs(i + 1)
            res = memo[i] = max(robCurrent, robNext)
            return res
        return dfs(0)