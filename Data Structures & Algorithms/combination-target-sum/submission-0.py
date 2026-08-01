class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, remaining):
            if remaining == 0:
                ans.append(path.copy())
                return
            elif remaining < 0:
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, remaining - nums[j])
                path.pop()
        dfs(0, target)
        return ans