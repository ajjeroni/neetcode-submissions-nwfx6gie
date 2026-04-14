class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # lets check the rows
        for row in board:
            nums = set()
            for num in row:
                if num in nums and num != '.':
                    return False
                if num != '.':
                    nums.add(num)
        print('Rows are good')

        # lets check the columns
        for col in range(9):
            nums = set()
            for row in board:
                if row[col] in nums and row[col] != '.':
                    return False
                if row[col] != '.': 
                    nums.add(row[col])
        print('Columns are good')

        # lets check squares 
        for i in range(0, 9, 3):
            for p in range(0, 9, 3):
                nums = set()
                for j in range(3):
                    for k in range(3):
                        if board[i + j][p + k] in nums and board[i + j][p + k] != '.':
                            return False
                        if board[i + j][p + k] != '.':
                            nums.add(board[i + j][p + k])
        print('Squares are bad')

        return True






