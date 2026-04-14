class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        l, r = 0, num_rows * num_cols - 1
        while l <= r:
            m = (l+r) // 2
            row = m // num_cols
            col = m % num_cols

            if target < matrix[row][col]:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
            
        return False