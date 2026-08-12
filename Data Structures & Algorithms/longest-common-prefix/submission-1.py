class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currChar = set()
        currIdx = 0
        ans = ""
        while True:
            for i in range(len(strs)):
                if currIdx < len(strs[i]):
                    currChar.add(strs[i][currIdx]) 
                else:
                    return ans
            if len(currChar) > 1:
                return ans
            ans += currChar.pop()
            currChar = set()
            currIdx += 1
        return ans