class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        have = start = left = 0
        tCount = Counter(t)
        need = len(tCount)
        minLen = float('inf')
        hm = defaultdict(int)

        for right, c in enumerate(s):
            hm[c] += 1
            if c in tCount and hm[c] == tCount[c]:
                have += 1
            while have == need:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left
                leftChar = s[left]
                hm[leftChar] -= 1
                if hm[leftChar] < tCount[leftChar]:
                    have -= 1
                left += 1
        return s[start : start + minLen] if minLen != float('inf') else ''