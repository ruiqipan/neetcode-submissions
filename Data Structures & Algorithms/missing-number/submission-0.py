class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumRange = sum(range(len(nums) + 1))
        sumList = sum(nums)
        return sumRange - sumList