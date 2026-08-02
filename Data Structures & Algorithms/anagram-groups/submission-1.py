class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            pattern = [0] * 26
            for c in s:
                pattern[ord(c) - ord('a')] += 1
            hm[tuple(pattern)].append(s)
        return list(hm.values())