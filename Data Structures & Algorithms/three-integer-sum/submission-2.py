class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0, n - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                ts = nums[i] + nums[left] + nums[right]
                if ts < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif ts > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans