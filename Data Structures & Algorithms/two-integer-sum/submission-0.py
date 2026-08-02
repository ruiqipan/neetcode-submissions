class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int) # key = num, val = index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hm.keys():
                return [hm[complement], i]
            if num not in hm.keys():
                hm[num] = i
        return [-1, -1]