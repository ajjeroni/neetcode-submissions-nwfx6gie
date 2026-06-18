class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # print(matrix)
        self.preSums = [[] for i in range(len(matrix))]
        
        for i,row in enumerate(matrix):
            # print(row)
            summ = 0
            for col in row:
                # print(col)
                summ += col
                self.preSums[i].append(summ)
            i += 1
        
        for i in range(len(self.preSums[0])):
            for j in range(1, len(self.preSums)):
                self.preSums[j][i] += self.preSums[j - 1][i]
        # print(self.preSums)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_left = self.preSums[row2][col2]
        top = self.preSums[row1 - 1][col2] if row1 > 0 else 0
        left_bottom = self.preSums[row2][col1 - 1] if col1 > 0 else 0
        left_top = self.preSums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        left = left_bottom - left_top
        return (bottom_left - (top + left))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)