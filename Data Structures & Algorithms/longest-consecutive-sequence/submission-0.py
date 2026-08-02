class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in numset:
                curr = num
                length = 1
                while curr + 1 in numset:
                    length += 1
                    curr = curr + 1
                ans = max(ans, length)
        return ans