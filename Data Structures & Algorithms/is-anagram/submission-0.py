class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sCount = Counter(s)
        tCount = Counter(t)
        return sCount == tCount