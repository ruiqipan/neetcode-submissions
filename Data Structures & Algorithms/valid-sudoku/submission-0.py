class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            seen = set()
            for c in range(cols):
                e = board[r][c]
                if e == '.':
                    continue
                if e in seen:
                    return False
                seen.add(e)
        
        for c in range(cols):
            seen = set()
            for r in range(rows):
                e = board[r][c]
                if e == '.':
                    continue
                if e in seen:
                    return False
                seen.add(e)

        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (sq // 3) * 3 + i
                    c = (sq % 3) * 3 + j
                    e = board[r][c]
                    if e == '.':
                        continue
                    if e in seen:
                        return False
                    seen.add(e)
        return True