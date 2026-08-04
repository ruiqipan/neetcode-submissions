class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        tCount = Counter(t)
        hm = defaultdict(int)
        left = 0
        have = 0
        need = len(tCount)
        minLen = float('inf')
        charStart = 0

        for right, c in enumerate(s):
            hm[c] += 1.
            if c in tCount and hm[c] == tCount[c]:
                have += 1
            while have == need:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    charStart = left
                leftChar = s[left]
                left += 1
                if leftChar in tCount and hm[leftChar] == tCount[leftChar]:
                    have -= 1
                hm[leftChar] -= 1
        return s[charStart : (charStart + minLen)] if minLen != float('inf') else ''