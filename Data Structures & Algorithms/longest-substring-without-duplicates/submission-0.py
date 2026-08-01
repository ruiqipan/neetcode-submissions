class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(s)):
            hm[s[right]] += 1
            while hm[s[right]] > 1:
                hm[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans