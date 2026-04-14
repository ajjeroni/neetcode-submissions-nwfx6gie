class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, m_cols = len(matrix), len(matrix[0])
        l, r = 0, n_rows * m_cols - 1
        while l <= r:
            m = (l+r) // 2
            row = m // m_cols
            col = m % m_cols

            if target < matrix[row][col]:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
            
        return False