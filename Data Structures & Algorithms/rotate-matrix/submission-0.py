class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        newMatrix = [[0] * n for i in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n):
                newMatrix[j][i] = matrix[-i + n + -1][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = newMatrix[i][j]


            