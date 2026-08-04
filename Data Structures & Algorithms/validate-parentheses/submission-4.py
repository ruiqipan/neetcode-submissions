class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stk = []

        for c in s:
            if c not in bracketMap:
                stk.append(c)
            else:
                if not stk:
                    return False
                if stk[-1] != bracketMap[c]:
                    return False
                else:
                    stk.pop()
        if stk:
            return False
        return True