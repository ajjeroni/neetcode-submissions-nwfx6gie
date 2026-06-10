class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                if num in rows[r] or num in cols[c]:
                    return False
                elif num in subs[r//3][c//3]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                subs[r//3][c//3].add(num)

        return True