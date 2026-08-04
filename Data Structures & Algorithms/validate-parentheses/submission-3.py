class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        openBrackets = ["(", "[", "{"]
        closedBrackets = [")", "]", "}"]

        for c in s:
            if c in openBrackets:
                stk.append(c)
            if c in closedBrackets:
                if not stk:
                    return False
                top = stk[-1]
                if (
                    top == openBrackets[0] and c == closedBrackets[0]
                    or top == openBrackets[1] and c == closedBrackets[1]
                    or top == openBrackets[2] and c == closedBrackets[2]
                ):
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True
