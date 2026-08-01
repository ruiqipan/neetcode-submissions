class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int) # index = num, val = freq
        for num in nums:
            hm[num] += 1
        
        bucket = [[] for _ in range (len(nums) + 1)] # index = freq, val = num
        for num, freq in hm.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ans.append(num)
            if len(ans) == k:
                break
        return ans